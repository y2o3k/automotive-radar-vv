"""Local visual FCW lab. Compile once; execute the C target for every requested run."""
import argparse
import csv
import json
import math
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
from urllib.parse import parse_qs, urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BINARY = HERE / '.build' / 'fcw'
COMPILED_SOURCE = ''
SCENARIOS = {
    'approach': {'name': '앞차에 접근', 'range_m': 30, 'ego_mps': 20, 'target_mps': 10},
    'steady': {'name': '같은 속도로 주행', 'range_m': 30, 'ego_mps': 20, 'target_mps': 20},
    'away': {'name': '앞차가 멀어짐', 'range_m': 30, 'ego_mps': 20, 'target_mps': 25},
}

def build():
    global COMPILED_SOURCE
    BINARY.parent.mkdir(parents=True, exist_ok=True)
    source = (HERE / 'fcw.c').read_text()
    subprocess.run(['cc', '-std=c99', '-Wall', '-Wextra', '-Werror',
                    str(HERE / 'fcw.c'), '-o', str(BINARY)], check=True, timeout=30)
    COMPILED_SOURCE = source

def evaluate(inputs):
    text = ''.join(f'{distance:.12g} {velocity:.12g}\n' for distance, velocity in inputs)
    result = subprocess.run([str(BINARY)], input=text, text=True, capture_output=True,
                            check=True, timeout=5)
    rows = [json.loads(line) for line in result.stdout.splitlines()]
    if len(rows) != len(inputs):
        raise ValueError('C output count does not match input count')
    return rows

def test_cases():
    with (ROOT / 'testcases/test_cases.csv').open(newline='') as stream:
        cases = list(csv.DictReader(stream))
    actual = evaluate([(float(c['range_m']), float(c['relative_velocity_mps'])) for c in cases])
    for case, observed in zip(cases, actual):
        expected_ttc = float(case['expected_ttc_s']) if case['expected_ttc_s'] else None
        actual_ttc = observed['ttc_s']
        ttc_ok = (actual_ttc is None and expected_ttc is None) or (
            actual_ttc is not None and expected_ttc is not None
            and math.isclose(actual_ttc, expected_ttc, rel_tol=1e-9, abs_tol=1e-9))
        case.update(actual_ttc_s=actual_ttc, actual_fcw=observed['fcw'],
                    passed=ttc_ok and observed['fcw'] == case['expected_fcw'])
    return cases

def run_scenario(identifier):
    spec = SCENARIOS[identifier]
    velocity = spec['target_mps'] - spec['ego_mps']
    frames = [{'time_s': tick / 50, 'range_m': round(spec['range_m'] + velocity * tick / 50, 8),
               'relative_velocity_mps': velocity} for tick in range(126)]
    actual = evaluate([(f['range_m'], velocity) for f in frames])
    for frame, result in zip(frames, actual):
        # Independent requirement oracle: compare distance to the 2-second travel distance.
        expected = 'ON' if velocity < 0 and frame['range_m'] <= -velocity * 2 else 'OFF'
        frame.update(result, expected_fcw=expected, passed=result['fcw'] == expected)
    return {'scenario': spec, 'frames': frames, 'cases': test_cases(),
            'source': COMPILED_SOURCE, 'step_s': .02,
            'execution': 'Compiled C on host; precomputed trace replay; simulated time'}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlparse(self.path)
        try:
            if route.path == '/api/run':
                identifier = parse_qs(route.query).get('scenario', ['approach'])[0]
                if identifier not in SCENARIOS:
                    self.send_error(400, 'Unknown scenario')
                    return
                body = json.dumps(run_scenario(identifier), ensure_ascii=False).encode()
                mime = 'application/json; charset=utf-8'
            elif route.path in ('/', '/app.js', '/styles.css'):
                filename = 'index.html' if route.path == '/' else route.path[1:]
                body = (HERE / 'web' / filename).read_bytes()
                mime = {'index.html': 'text/html', 'app.js': 'text/javascript',
                        'styles.css': 'text/css'}[filename] + '; charset=utf-8'
            else:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header('Content-Type', mime)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(body)
        except (OSError, ValueError, subprocess.SubprocessError):
            self.send_error(500, 'Simulation failed; check server terminal')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    build()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    print(f'FCW visual lab: http://127.0.0.1:{args.port}', flush=True)
    server.serve_forever()
