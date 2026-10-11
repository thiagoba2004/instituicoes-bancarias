"""Verify a fetched remote commit and canonical Git blobs, without mutation."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def verify(commit):
    remote = git('rev-parse', 'origin/main').decode().strip()
    if commit != remote:
        raise ValueError('REMOTE_COMMIT_MISMATCH')
    paths = git('diff-tree', '--no-commit-id', '--name-only', '-r', commit).decode().splitlines()
    files = []
    for path in paths:
        raw = git('show', commit + ':' + path)
        blob = git('rev-parse', commit + ':' + path).decode().strip()
        local_blob = git('hash-object', '--path=' + path, path).decode().strip()
        if blob != local_blob:
            raise ValueError('WORKTREE_BLOB_MISMATCH:' + path)
        files.append({'path': path, 'git_blob': blob, 'canonical_sha256': hashlib.sha256(raw).hexdigest()})
    return {'commit': commit, 'remote_ref': 'origin/main', 'remote_commit': remote,
            'method': 'Authorized fetch followed by Git object readback and worktree filter hash comparison',
            'classification': 'S0_PUBLICO', 'files_verified': len(files), 'files': files}

if __name__ == '__main__':
    result = verify(sys.argv[1])
    destination = ROOT / sys.argv[2]
    if not destination.resolve().is_relative_to(ROOT):
        raise ValueError('DESTINATION_OUTSIDE_PRJ')
    destination.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(result['commit'], result['files_verified'], 'blobs verified')
