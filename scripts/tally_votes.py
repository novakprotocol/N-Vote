import json, sys
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=root/"data"
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
req=json.loads((data/"requests.json").read_text(encoding="utf-8")).get("records",[])
def key(x):
    r=x.get("reactions",{}); labels=set(x.get("labels",[]))
    return (-(1 if "approved-now" in labels else 0), -float(x.get("score",0)), -int(r.get("rocket",0)), -int(r.get("+1",0)), str(x.get("opened_at","9999")))
active=[x for x in req if x.get("state","open")=="open"]
records=[{"scope":"overall","top5":sorted(active,key=key)[:5]}]
for area in sorted({x.get("area","other") for x in active}):
    records.append({"scope":"area","area":area,"top5":sorted([x for x in active if x.get("area")==area],key=key)[:5]})
out={"schema":"n-vote.public-data.v1.friday_top5","generated_at":now(),"source_repo":"novakprotocol/N-Vote","public_private_boundary":"Public votes are public signals only. Owner approval is required before private work.","records":records}
(data/"friday-top5.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print("Built data/friday-top5.json")
