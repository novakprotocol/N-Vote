import json, sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
files=["areas.json","requests.json","votes.json","friday-top5.json","approved-now.json","public-roadmap.json"]
errs=[]
for f in files:
    p=root/"data"/f
    if not p.exists(): errs.append(f"missing {f}"); continue
    try: d=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: errs.append(f"{f}: {e}"); continue
    for k in ["schema","generated_at","source_repo","public_private_boundary","records"]:
        if k not in d: errs.append(f"{f}: missing {k}")
    if d.get("source_repo")!="novakprotocol/N-Vote": errs.append(f"{f}: bad source_repo")
    if not str(d.get("schema","")).startswith("n-vote.public-data.v1"): errs.append(f"{f}: bad schema")
    if not isinstance(d.get("records"),list): errs.append(f"{f}: records not list")
    b=str(d.get("public_private_boundary","")).lower()
    if "owner approval" not in b: errs.append(f"{f}: boundary missing owner approval")
if errs:
    print("N-Vote data contract check failed:"); print("\n".join("- "+e for e in errs)); sys.exit(1)
print("N-Vote data contract check passed.")
