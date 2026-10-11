"""Read-only external source tests. All output stays in this PRJ; no bytecode."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'governanca/testes-sciv'
py = sys.executable

def run(name, arguments, cwd):
    result = subprocess.run([py, '-B', *arguments], cwd=cwd, capture_output=True)
    (OUT / (name + '.log')).write_bytes(result.stdout + result.stderr)
    print(name, result.returncode, (result.stdout + result.stderr).decode('utf-8', errors='replace')[-800:])
    return {'name': name, 'exit_code': result.returncode}

def main():
    # Regenerate only the managed block from the immutable preflight commit.
    from provision import BASE, compose, baseline
    original = baseline()
    template_path = ROOT.parent / 'gerador-de-agents/templates/SCIV_BOOTSTRAP.example.md'
    template = template_path.read_bytes()
    adapter = ROOT / 'adaptadores/chatgpt/INSTRUCOES.md'
    adapter.write_bytes(compose(original, template, authorized=True))
    proof = json.loads((OUT / 'composition.json').read_text())
    proof['composed_adapter_sha256'] = hashlib.sha256(adapter.read_bytes()).hexdigest()
    (OUT / 'composition.json').write_text(json.dumps(proof, indent=2) + '\n')
    results = [
        run('local', ['-m', 'unittest', 'discover', '-s', str(OUT), '-p', 'test_local.py', '-v'], ROOT),
        run('generator', ['-m', 'unittest', 'test_sciv_bootstrap', 'test_project_creation_gate', '-v'], ROOT.parent / 'gerador-de-agents/tools'),
        run('runtime', ['-m', 'unittest', 'test_sciv_archive', 'test_sciv_security', 'test_sciv_essential', 'test_sciv_per_project', 'test_sciv_mailbox', 'test_sciv_publication', '-v'], ROOT.parent / 'governanca-geral-modelos-ia/runtime'),
        run('gate-sciv', [str(ROOT.parent / 'gerador-de-agents/tools/project_creation_gate.py'), '--project-root', str(ROOT), '--route', 'A', '--gate', 'sciv'], ROOT)
    ]
    (OUT / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
    return 0 if all(item['exit_code'] == 0 for item in results) else 1

if __name__ == '__main__':
    raise SystemExit(main())
