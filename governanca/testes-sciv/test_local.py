import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(ROOT.parent / 'gerador-de-agents/tools'))
sys.path.insert(0, str(ROOT.parent / 'governanca-geral-modelos-ia/runtime'))
from provision import compose, BASE, BEGIN, END, baseline
from sciv_bootstrap import integrate


class LocalContractTests(unittest.TestCase):
    def test_original_bytes_preserved(self):
        original = baseline()
        current = (ROOT / 'adaptadores/chatgpt/INSTRUCOES.md').read_bytes()
        start = current.index(BEGIN.encode())
        end = current.index(END.encode()) + len(END.encode()) + 2
        self.assertEqual(current[:start] + current[end:], original)
        proof = json.loads((ROOT / 'governanca/testes-sciv/composition.json').read_text())
        self.assertEqual(hashlib.sha256(original).hexdigest(), proof['original_adapter_sha256'])
        self.assertEqual(hashlib.sha256(current).hexdigest(), proof['composed_adapter_sha256'])

    def test_idempotent_upstream_composition_offline_fixture_only(self):
        state = json.loads((ROOT / 'comunicados/SCIV_STATE.json').read_text())
        # These are explicitly synthetic unit-test dependencies, NOT binding evidence.
        profile = {'project_code': state['project_code'], 'project_ref': state['repository'],
                   'sciv_bootstrap': dict(enabled=True, mode='ON_DEMAND',
                       binding_evidence='OFFLINE_FIXTURE_NOT_REAL_BINDING',
                       github_read_evidence='OFFLINE_FIXTURE', provisioning_evidence='OFFLINE_FIXTURE')}
        original = (ROOT / 'adaptadores/chatgpt/INSTRUCOES.md').read_bytes().decode('utf-8')
        self.assertEqual(integrate(original, profile, state), original)

    def test_unauthorized_composition_denied(self):
        with self.assertRaisesRegex(ValueError, 'HANDOFF_REQUIRED'):
            compose(b'', b'', authorized=False)

    def test_corrupt_block_not_overwritten(self):
        with self.assertRaisesRegex(ValueError, 'REQUIRES_REVIEW'):
            compose(BEGIN.encode(), b'', authorized=True)

    def test_no_fabricated_messages(self):
        state = json.loads((ROOT / 'comunicados/SCIV_STATE.json').read_text())
        for key in ('inbox', 'outbox', 'inbox_history', 'outbox_history'):
            self.assertEqual([p.name for p in (ROOT / state[key]).iterdir()], ['README.md'])

    def test_native_gates_not_promoted(self):
        state = json.loads((ROOT / 'PROJECT_STATE.json').read_text(encoding='utf-8'))
        for key in ('c3_native_installation_verified', 'chatgpt_project_binding_verified', 'a6_accepted'):
            self.assertIs(state[key], False)

    def test_normal_task_does_not_access_store(self):
        from sciv_essential import consult_on_demand
        class NoAccess:
            def __getattr__(self, name):
                raise AssertionError('Unexpected mailbox access: ' + name)
        result = consult_on_demand(NoAccess(), 'PRJ-000022', request=False, route=None)
        self.assertEqual(result['state'], 'NOT_REQUESTED_NO_MAILBOX_READ')

    def test_branch_mismatch_with_current_main_route(self):
        from test_sciv_archive import ArchiveTests
        from sciv_mailbox import MailboxError
        fixture = ArchiveTests()
        fixture.setUp()
        fixture.store.branch = 'unauthorized-reference'
        with self.assertRaisesRegex(MailboxError, 'REFERENCE_MISMATCH'):
            fixture.plan()


if __name__ == '__main__':
    unittest.main()
