"""F004 only: immutable dependency snapshots, no provisioning or adapter writes."""
import hashlib
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
GEN = ROOT / '.f004-sources/generator'
G0 = ROOT / '.f004-sources/g0-snapshot'
OUT = ROOT / 'governanca/testes-sciv/retest-2026-10-11'
BASE = '369cd41'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_suite():
    os.environ['F004_GENERATOR_ROOT'] = str(GEN)
    os.environ['F004_G0_ROOT'] = str(G0)
    import test_local
    # test_local's legacy sibling paths must not select stale G0 modules.
    sys.path[:0] = [str(GEN / 'tools'), str(G0 / 'runtime')]
    from provision import baseline, compose, BEGIN, END

    def reconciled_integrity(self):
        adapter = ROOT / 'adaptadores/chatgpt/INSTRUCOES.md'
        current = adapter.read_bytes().replace(b'\r\n', b'\n')
        canonical = subprocess.check_output(
            ['git', 'show', BASE + ':adaptadores/chatgpt/INSTRUCOES.md'], cwd=ROOT)
        self.assertEqual(current, canonical.replace(b'\r\n', b'\n'))
        historic = subprocess.check_output(
            ['git', 'show', '6700203:adaptadores/chatgpt/INSTRUCOES.md'], cwd=ROOT)
        def block(data):
            return data[data.index(BEGIN.encode()):data.index(END.encode()) + len(END.encode())]
        self.assertEqual(block(current), block(historic).replace(b'\r\n', b'\n'))
        proof = json.loads((ROOT / 'governanca/testes-sciv/composition.json').read_text())
        self.assertEqual(hashlib.sha256(baseline()).hexdigest(), proof['original_adapter_sha256'])
        template = (GEN / 'templates/SCIV_BOOTSTRAP.example.md').read_bytes()
        reconstructed = compose(baseline(), template, authorized=True)
        self.assertEqual(hashlib.sha256(reconstructed).hexdigest(), proof['composed_adapter_sha256'])
        self.assertEqual(reconstructed.replace(b'\r\n', b'\n'), historic.replace(b'\r\n', b'\n'))

    # G0 legitimately changed non-managed text at 5d140d0; preserve that newer
    # canonical adapter while retaining the original F003 composition proof.
    test_local.LocalContractTests.test_original_bytes_preserved = reconciled_integrity
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(test_local.LocalContractTests)
    with (OUT / 'local.log').open('w', encoding='utf-8') as stream:
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    sources = {name: {'path': str(Path(importlib.import_module(name).__file__).relative_to(ROOT)),
                      'sha256': sha(Path(importlib.import_module(name).__file__))}
               for name in ('sciv_bootstrap', 'sciv_essential', 'sciv_mailbox', 'test_sciv_archive')}
    (OUT / 'loaded-modules.json').write_text(json.dumps(sources, indent=2) + '\n')
    return {'name': 'local', 'tests': result.testsRun, 'failures': len(result.failures),
            'errors': len(result.errors), 'skipped': len(result.skipped), 'success': result.wasSuccessful()}


def command(name, args, cwd, expected=0):
    env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
    result = subprocess.run([sys.executable, '-B', *args], cwd=cwd, env=env, capture_output=True)
    (OUT / (name + '.log')).write_bytes(result.stdout + result.stderr)
    return {'name': name, 'arguments': args, 'cwd': str(cwd.relative_to(ROOT)),
            'exit_code': result.returncode, 'expected_exit_code': expected,
            'success': result.returncode == expected}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    sys.path[:0] = [str(Path(__file__).parent), str(GEN / 'tools'), str(G0 / 'runtime')]
    before = sha(ROOT / 'adaptadores/chatgpt/INSTRUCOES.md')
    if '--local-only' in sys.argv:
        saved = json.loads((OUT / 'results.json').read_text())
        saved['results'][0] = local_suite()
        saved['results'].append(command('controlled-sensitivity',
            ['auditorias/EA-000000-000034/ACT028/controlled-coverage-check.py'], G0))
        assert sha(ROOT / 'adaptadores/chatgpt/INSTRUCOES.md') == before
        (OUT / 'results.json').write_text(json.dumps(saved, indent=2) + '\n')
        print(json.dumps(saved['results'], indent=2))
        return 0 if all(x['success'] for x in saved['results']) else 1
    results = [local_suite(),
        command('generator', ['-m', 'unittest', 'discover', '-s', 'tools', '-p', 'test*.py', '-v'], GEN),
        command('runtime', ['-m', 'unittest', 'discover', '-s', 'runtime', '-p', 'test_sciv*.py', '-v'], G0),
        command('pep-offline', ['-m', 'unittest', 'discover', '-s', 'tools', '-p', 'test_r2_pep_offline.py', '-v'], G0),
        command('gate-sciv', [str(GEN / 'tools/project_creation_gate.py'), '--project-root', str(ROOT), '--route', 'A', '--gate', 'sciv'], ROOT),
        command('gate-bootstrap-expected-fail', [str(GEN / 'tools/project_creation_gate.py'), '--project-root', str(ROOT), '--route', 'A', '--gate', 'bootstrap'], ROOT, expected=1)]
    assert sha(ROOT / 'adaptadores/chatgpt/INSTRUCOES.md') == before
    (OUT / 'results.json').write_text(json.dumps({'python': sys.version, 'adapter_sha256_unchanged': before,
        'results': results}, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(results, indent=2))
    return 0 if all(x['success'] for x in results) else 1


if __name__ == '__main__':
    raise SystemExit(main())
