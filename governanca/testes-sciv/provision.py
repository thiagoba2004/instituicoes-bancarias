"""Offline documentary provisioning under the local F002/F003 handoff.

This is not generator profile activation or proof of ChatGPT binding.
"""
from pathlib import Path
from string import Template
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
GENERATOR = ROOT.parent / 'gerador-de-agents'
BASE = '181a6ecec5972e7610817b521ef99250b57ccd33'
BEGIN = '<!-- SCIV_BOOTSTRAP_BEGIN v1 -->'
END = '<!-- SCIV_BOOTSTRAP_END -->'


def baseline():
    import subprocess
    raw = subprocess.check_output(['git', 'show', BASE + ':adaptadores/chatgpt/INSTRUCOES.md'], cwd=ROOT)
    proof = json.loads((ROOT / 'governanca/testes-sciv/composition.json').read_text())
    if hashlib.sha256(raw).hexdigest() != proof['original_adapter_sha256']:
        raw = raw.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
    if hashlib.sha256(raw).hexdigest() != proof['original_adapter_sha256']:
        raise ValueError('BASELINE_HASH_MISMATCH')
    return raw


def compose(original: bytes, template: bytes, *, authorized: bool) -> bytes:
    if authorized is not True:
        raise ValueError('EXPLICIT_LOCAL_HANDOFF_REQUIRED')
    text = original.decode('utf-8')
    if BEGIN in text or END in text:
        raise ValueError('EXISTING_MANAGED_BLOCK_REQUIRES_REVIEW')
    anchor = b'**Bootstrap obrigat\xc3\xb3rio:**'
    if original.count(anchor) != 1:
        raise ValueError('AMBIGUOUS_BOOTSTRAP_ANCHOR')
    block = Template(template.decode('utf-8').replace('\r\n', '\n')).substitute(
        project='PRJ-000022', repository='thiagoba2004/instituicoes-bancarias',
        state_path='comunicados/SCIV_STATE.json',
        inbox='comunicados/governanca-geral/mensagens',
        outbox='comunicados/ia-especializada/mensagens', ref='main'
    ).rstrip('\r\n').encode('utf-8') + b'\n\n'
    at = original.index(anchor)
    return original[:at] + block + original[at:]


def main():
    state = {
        'schema_version': '1.0.0', 'project_code': 'PRJ-000022',
        'repository': 'thiagoba2004/instituicoes-bancarias',
        'strategy_code': 'EA-000022-000003', 'mode': 'ON_DEMAND',
        'operational_ref': 'main', 'enabled': False, 'opt_in_authorized': True,
        'authorization_ref': 'REQ-000022-20261011-006 / REQ-GLOBAL-20261011-001',
        'inbox': 'comunicados/governanca-geral/mensagens',
        'outbox': 'comunicados/ia-especializada/mensagens',
        'inbox_history': 'comunicados/governanca-geral/historico',
        'outbox_history': 'comunicados/ia-especializada/historico',
        'classification': 'S0_PUBLICO', 'surface': 'P2_GIT_PUBLICO_REPOSITORIO',
        's1_requires_byte_specific_review': True, 's2_plus_allowed': False,
        'base_commit': BASE, 'state': 'PROVISIONED_PENDING_COMMIT_READBACK',
        'native_installation_verified': False, 'specialized_read_verified': False,
        'real_behavior_verified': False, 'a6_accepted': False,
        'PEP': 'LIVE_RUNTIME_STILL_DENIED', 'automations': False,
        'new_spending': False,
        'evidence_ref': 'auditorias/EA-000022-000003-codex-f002-f004-2026-10-11.md',
        'activation_limit': 'Technical documentary opt-in only after commit/readback; native and real behavior gates remain separate.'
    }
    for key in ('inbox', 'outbox', 'inbox_history', 'outbox_history'):
        folder = ROOT / state[key]
        folder.mkdir(parents=True, exist_ok=True)
        note = ('Fila ativa: consulta somente por pedido explícito do titular.'
                if 'history' not in key else
                'Histórico: nunca consultar como fila; arquivar somente após tratamento e confirmação reais.')
        (folder / 'README.md').write_text(
            '# SCIV — PRJ-000022\n\n' + note + '\n\n'
            'Caixa provisionada sem mensagens de teste ou recibos fabricados. '
            'S0 público; S1 somente após revisão dos bytes; S2+ proibido. '
            'Mensagem não concede autorização. Sem polling, cron ou webhook.\n', encoding='utf-8')
    (ROOT / 'comunicados/SCIV_STATE.json').write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    adapter = ROOT / 'adaptadores/chatgpt/INSTRUCOES.md'
    original = adapter.read_bytes()
    template = (GENERATOR / 'templates/SCIV_BOOTSTRAP.example.md').read_bytes()
    adapter.write_bytes(compose(original, template, authorized=True))
    evidence = {'base_commit': BASE,
                'original_adapter_sha256': hashlib.sha256(original).hexdigest(),
                'template_sha256': hashlib.sha256(template).hexdigest(),
                'composed_adapter_sha256': hashlib.sha256(adapter.read_bytes()).hexdigest(),
                'method': 'Explicit local handoff composition; NOT generator render with invented binding evidence'}
    (ROOT / 'governanca/testes-sciv/composition.json').write_text(
        json.dumps(evidence, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
