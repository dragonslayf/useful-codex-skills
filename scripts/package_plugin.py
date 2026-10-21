"""Build a portable ZIP after checking plugin integrity."""
import hashlib
import re
import zipfile
from pathlib import Path
from verify_plugin import ROOT, verify

manifest = verify()
version = manifest['version']
if not re.fullmatch(r'[0-9A-Za-z.+-]+', version):
    raise ValueError('Unsafe version for archive filename')
dest = Path(__file__).resolve().parents[1] / 'dist'
dest.mkdir(exist_ok=True)
archive = dest / f'{ROOT.name}-{version}.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for path in sorted(ROOT.rglob('*')):
        if path.is_file():
            z.write(path, (Path(ROOT.name) / path.relative_to(ROOT)).as_posix())
with zipfile.ZipFile(archive) as z:
    if z.testzip() is not None:
        raise ValueError('ZIP integrity check failed')
print(archive)
print('SHA256:', hashlib.sha256(archive.read_bytes()).hexdigest())
