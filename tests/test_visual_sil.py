import importlib.util
from pathlib import Path
import subprocess
import unittest

SPEC = importlib.util.spec_from_file_location('visual_sil', Path(__file__).resolve().parents[1] / 'sil/server.py')
sil = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sil)

class VisualSilTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        sil.build()

    def test_existing_csv_cases_on_compiled_c(self):
        cases = sil.test_cases()
        self.assertEqual(len(cases), 6)
        self.assertTrue(all(case['passed'] for case in cases))

    def test_warning_changes_at_boundary_not_before(self):
        frames = sil.run_scenario('approach')['frames']
        self.assertEqual((frames[49]['time_s'], frames[49]['fcw']), (.98, 'OFF'))
        self.assertEqual((frames[50]['time_s'], frames[50]['ttc_s'], frames[50]['fcw']), (1, 2, 'ON'))
        self.assertEqual((frames[-1]['time_s'], frames[-1]['range_m']), (2.5, 5))
        self.assertTrue(all(frame['passed'] for frame in frames))

    def test_nonclosing_scenarios(self):
        for scenario in ['steady', 'away']:
            frames = sil.run_scenario(scenario)['frames']
            self.assertTrue(all(f['ttc_s'] is None and f['fcw'] == 'OFF' for f in frames))

    def test_c_rejects_invalid_inputs(self):
        for value in ['-1 -10\n', 'nan -10\n', '20 inf\n', 'invalid\n']:
            result = subprocess.run([str(sil.BINARY)], input=value, text=True, capture_output=True, timeout=5)
            self.assertEqual(result.returncode, 2)

if __name__ == '__main__':
    unittest.main()
