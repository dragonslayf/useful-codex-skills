"""Validate the portable plugin manifest and file hashes using only stdlib."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'plugins/codex-personal-environment'

def verify(refresh=False):
    manifest = json.loads((ROOT / '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
    if manifest.get('name') != ROOT.name or manifest.get('skills') != './skills/':
        raise ValueError('Unexpected plugin name or skills entry point')
    required_skills = ('command-journal', 'yinxiang-skill')
    missing = [name for name in required_skills if not (ROOT / f'skills/{name}/SKILL.md').is_file()]
    if missing:
        raise ValueError('Missing required skills: ' + ', '.join(missing))
    files = {}
    for path in sorted(ROOT.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Unexpected symbolic link: {path}')
        if path.is_file() and path != ROOT / 'SHA256SUMS.json':
            files[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    checksums = ROOT / 'SHA256SUMS.json'
    if refresh:
        checksums.write_text(
            json.dumps(files, ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8',
            newline='\n',
        )
    expected = json.loads(checksums.read_text(encoding='utf-8'))
    if files != expected:
        changed = sorted(k for k in files.keys() | expected.keys() if files.get(k) != expected.get(k))
        raise ValueError('File integrity mismatch: ' + ', '.join(changed))
    print(f'Validated {len(files)} files: {manifest["name"]} {manifest["version"]}')
    return manifest

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true', help='Replace checksums with current reviewed file hashes')
    verify(parser.parse_args().refresh)
