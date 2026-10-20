"""Fresh-copy, fresh-venv validation; installs no packages and preserves the run."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
FILES = ['project1/engine.py','project1/research.py','project1/test_engine.py','project1/app.py',
         'Pro-Forma Financial Statements/proforma.COHR.py']


def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    folder=Path(tempfile.mkdtemp(prefix='cohr-project1-cold-'))
    workspace=folder/'workspace'
    env=folder/'environment'
    events=[f'UTC run: {stamp}',f'Source Python: {sys.version}',f'Fresh copy: {workspace}',
            'No third-party packages installed; virtual environment created without pip.',
            'This is an AI-assisted cold run, NOT the student AI-off changed-input exercise.']
    def execute(args,cwd=None):
        events.append('COMMAND: '+' '.join(str(x) for x in args))
        result=subprocess.run([str(x) for x in args],cwd=cwd,text=True,capture_output=True)
        events.extend([result.stdout,result.stderr,f'EXIT: {result.returncode}'])
        if result.returncode:
            raise RuntimeError(f'Cold run failed: {args}')
    status='FAIL'
    hashes={}
    try:
        for rel in FILES:
            src=ROOT/rel;dst=workspace/rel
            dst.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(src,dst)
            hashes[rel]=hashlib.sha256(src.read_bytes()).hexdigest()
            assert hashlib.sha256(dst.read_bytes()).hexdigest()==hashes[rel]
        execute([sys.executable,'-m','venv','--without-pip',env])
        python=env/('Scripts/python.exe' if sys.platform=='win32' else 'bin/python')
        execute([python,'project1/test_engine.py'],workspace)
        execute([python,'project1/engine.py'],workspace)
        execute([python,'project1/app.py','--export'],workspace)
        result=json.loads((workspace/'outputs/project1-base.json').read_text())
        assert result['all_checks_pass']
        assert len(result['scenarios'])==4 and not result['scenarios'][-1]['valid']
        assert len(result['peers']['single_peer_references_per_share'])==3
        events.append('Verified: base articulates, causal cases retained, sticky-capex stress fails, peer outputs present, static HTML exported.')
        status='PASS'
    finally:
        events += ['Source hashes: '+json.dumps(hashes,sort_keys=True),
                   'Temporary environment/copy retained; no source file removed.',f'FINAL STATUS: {status}']
        output=ROOT/'outputs';output.mkdir(exist_ok=True)
        log=output/f'cold-run-{stamp}.txt'
        log.write_text('\n'.join(events)+'\n')
        print(f'{status}: {log}')
        print(f'Preserved environment: {folder}')


if __name__=='__main__':main()
