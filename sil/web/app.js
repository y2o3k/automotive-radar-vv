const $ = id => document.getElementById(id);
let data, index = 0, playing = false, lastTime = null, animation;
const seconds = value => value == null ? '—' : `${Number(value).toFixed(2)} s`;
function pause() { playing = false; lastTime = null; cancelAnimationFrame(animation); $('play').textContent = '▶ 재생'; }
function render() {
  const frame = data.frames[index], on = frame.fcw === 'ON';
  $('time').innerHTML = `${frame.time_s.toFixed(2)} <em>s</em>`;
  $('range').innerHTML = `${frame.range_m.toFixed(1)} <em>m</em>`;
  $('ttc').innerHTML = frame.ttc_s == null ? '— <em>비접근</em>' : `${frame.ttc_s.toFixed(2)} <em>s</em>`;
  $('target').setAttribute('transform', `translate(${110 + frame.range_m * 11} 88)`);
  $('distance-line').setAttribute('d', `M110 160 H${110 + frame.range_m * 11}`);
  $('distance-label').setAttribute('x', 110 + frame.range_m * 5.5);
  $('distance-label').textContent = `${frame.range_m.toFixed(1)} m`;
  $('warning').classList.toggle('on', on);
  $('warning').innerHTML = `경고 ${frame.fcw}<span>${on ? '전방 충돌 경고 발생' : '충돌 경고 없음'}</span>`;
  $('expected').textContent = frame.expected_fcw;
  $('actual').textContent = frame.fcw;
  $('verdict').textContent = frame.passed ? 'PASS' : 'FAIL';
  $('verdict').className = frame.passed ? 'pass' : 'fail';
  $('timeline').value = index;
  $('step').disabled = index === data.frames.length - 1;
}
function tick(now) {
  if (!playing) return;
  if (lastTime == null) lastTime = now;
  const steps = Math.floor((now - lastTime) / 20);
  if (steps > 0) { index = Math.min(data.frames.length - 1, index + steps); lastTime += steps * 20; render(); }
  if (index === data.frames.length - 1) { pause(); return; }
  animation = requestAnimationFrame(tick);
}
async function run() {
  pause();
  document.querySelectorAll('button, select, input').forEach(el => el.disabled = true);
  $('status').textContent = '실제 C 프로그램 실행 중…';
  try {
    const response = await fetch(`/api/run?scenario=${encodeURIComponent($('scenario').value)}`);
    if (!response.ok) throw new Error('실행 오류');
    data = await response.json(); index = 0;
    $('source').textContent = data.source;
    $('cases').replaceChildren();
    for (const item of data.cases) {
      const row = document.createElement('tr');
      [item.test_case_id, `${Number(item.range_m)} m / ${Number(item.relative_velocity_mps)} m/s`,
       `${seconds(item.expected_ttc_s === '' ? null : Number(item.expected_ttc_s))} / ${item.expected_fcw}`,
       `${seconds(item.actual_ttc_s)} / ${item.actual_fcw}`, item.passed ? 'PASS' : 'FAIL'].forEach((value, n) => {
        const cell = document.createElement('td'); cell.textContent = value;
        if (n === 4) cell.className = item.passed ? 'pass' : 'fail';
        row.appendChild(cell);
      });
      row.title = item.requirement_id; $('cases').appendChild(row);
    }
    const passed = data.cases.filter(c => c.passed).length;
    $('case-count').textContent = `${passed} / ${data.cases.length} PASS`;
    $('case-count').className = passed === data.cases.length ? 'pass' : 'fail';
    $('status').textContent = `C 실행 완료 · ${data.frames.length}개 프레임 재생 준비`;
    $('hint').textContent = $('scenario').value === 'approach'
      ? '재생 후 1.00초에 TTC = 2.00초, 경고 ON이 되는지 확인하세요.'
      : '접근하지 않는 상황입니다. TTC는 계산하지 않고 경고 OFF를 유지해야 합니다.';
    document.querySelectorAll('button, select, input').forEach(el => el.disabled = false);
    $('boundary').disabled = $('scenario').value !== 'approach';
    render();
  } catch (error) {
    data = null;
    $('status').textContent = '실행 실패. 로컬 서버를 확인한 뒤 다시 실행하세요.';
    $('rerun').disabled = false; $('scenario').disabled = false;
  }
}
$('play').onclick = () => { if (playing) { pause(); return; } if (index === data.frames.length - 1) index = 0; playing = true; $('play').textContent = 'Ⅱ 일시정지'; render(); animation = requestAnimationFrame(tick); };
$('step').onclick = () => { pause(); index = Math.min(index + 1, data.frames.length - 1); render(); };
$('reset').onclick = () => { pause(); index = 0; render(); };
$('boundary').onclick = () => { pause(); index = 50; render(); };
$('timeline').oninput = event => { pause(); index = Number(event.target.value); render(); };
$('scenario').onchange = run;
$('rerun').onclick = run;
run();
