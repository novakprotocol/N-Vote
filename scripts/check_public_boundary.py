import json, re, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
errs=[]
secret=[r"ghp_[A-Za-z0-9_]{20,}",r"github_pat_[A-Za-z0-9_]{20,}",r"AKIA[0-9A-Z]{16}",r"BEGIN [A-Z ]*PRIVATE KEY",r"Authorization:\\s*Bearer\\s+[A-Za-z0-9._-]{8,}"]
local=[r"\\b[A-Za-z]:[\\\\/](?![\\\\/])",r"/Users/",r"/home/",r"Documents/Repos",r"Desktop/",r"Downloads/"]
private_markers=[".nstack/runs",".n-suite-evidence",".env",".venv"]
workflow_blockers=["n-ai-runner","safe-bridge",".nstack/runs","repository_dispatch","workflow_run","private packet"]
def scan(path,text):
    for pat in secret+local:
        if re.search(pat,text): errs.append(f"{path}: forbidden pattern {pat}")
    for m in private_markers:
        if m in text: errs.append(f"{path}: private marker {m}")
for p in (root/"data").glob("*.json"):
    t=p.read_text(encoding="utf-8"); scan(p,t)
    json.loads(t)
for p in [root/"README.md",root/"docs/PUBLIC_PRIVATE_BOUNDARY.md",root/"site/app.js"]:
    if p.exists(): scan(p,p.read_text(encoding="utf-8"))
for p in (root/".github/workflows").glob("*.yml"):
    t=p.read_text(encoding="utf-8").lower(); scan(p,t)
    for m in workflow_blockers:
        if m in t: errs.append(f"{p}: workflow blocker {m}")
if errs:
    print("N-Vote public boundary check failed:"); print("\n".join("- "+e for e in errs)); sys.exit(1)
print("N-Vote public boundary check passed.")
