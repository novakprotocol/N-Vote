import json, py_compile, subprocess, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=["README.md","COMMANDS.md","AGENTS.md","NEXT_RUN.md","app.manifest.json","app.surface.json","site/index.html","site/app.js","site/style.css","site/assets/n-vote-logo.svg",".github/workflows/quality-gate.yml",".github/workflows/build-public-data.yml",".github/workflows/friday-top5.yml",".github/workflows/pages.yml",".github/ISSUE_TEMPLATE/feature_request.yml",".github/ISSUE_TEMPLATE/bug_report.yml",".github/ISSUE_TEMPLATE/vote_nomination.yml",".github/ISSUE_TEMPLATE/config.yml","scripts/build_public_data.py","scripts/tally_votes.py","scripts/check_public_boundary.py","scripts/check_data_contract.py","scripts/quality_gate.py","docs/PUBLIC_PRIVATE_BOUNDARY.md","docs/VOTING_MODEL.md","docs/OWNER_APPROVAL.md","docs/OVERLAY_INTEGRATION.md","features/FEATURE_LEDGER.json"]
errs=[f"missing {x}" for x in required if not (root/x).exists()]
for p in (root/"scripts").glob("*.py"):
    try: py_compile.compile(str(p), doraise=True)
    except Exception as e: errs.append(f"{p}: {e}")
for s in ["check_public_boundary.py","check_data_contract.py"]:
    if subprocess.run([sys.executable,str(root/"scripts"/s)],cwd=root).returncode: errs.append(f"{s} failed")
txt=(root/"app.surface.json").read_text(encoding="utf-8")
for c in ["n-vote.open_site","n-vote.submit_request","n-vote.view_top5","n-vote.view_approved_now","n-vote.refresh_public_data","n-vote.copy_private_handoff_stub"]:
    if c not in txt: errs.append(f"missing command {c}")
html=(root/"site/index.html").read_text(encoding="utf-8")
for b in ["Submit request","Open request","View Friday top 5","View approved now","Read public/private boundary","Read how voting works"]:
    if b not in html: errs.append(f"missing button {b}")
if errs:
    print("N-Vote quality gate failed:"); print("\n".join("- "+e for e in errs)); sys.exit(1)
print("N-Vote quality gate passed.")
