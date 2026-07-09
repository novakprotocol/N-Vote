import json, os, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]; data=root/"data"; repo=os.getenv("GITHUB_REPOSITORY","novakprotocol/N-Vote")
boundary="Public issues and reactions are public signals only. Owner approval is required before private work."
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def write(name,records): (data/name).write_text(json.dumps({"schema":"n-vote.public-data.v1."+name.replace(".json","").replace("-","_"),"generated_at":now(),"source_repo":"novakprotocol/N-Vote","public_private_boundary":boundary,"records":records},indent=2,sort_keys=True)+"\n",encoding="utf-8")
def api(path):
    token=os.getenv("GITHUB_TOKEN"); h={"Accept":"application/vnd.github+json","User-Agent":"n-vote"}
    if token: h["Authorization"]="Bearer "+token
    with urllib.request.urlopen(urllib.request.Request("https://api.github.com/repos/"+repo+path,headers=h),timeout=30) as r: return json.load(r)
def score(r): return r.get("+1",0)+2*r.get("heart",0)+3*r.get("rocket",0)+0.5*r.get("eyes",0)-r.get("-1",0)
records=[]
try:
    issues=api('/issues?state=all&per_page=100')
    for i in issues:
        if "pull_request" in i: continue
        labels=[l["name"] for l in i.get("labels",[])]
        area=next((x.split(":",1)[1] for x in labels if x.startswith("area:")),"other")
        react=api(f'/issues/{i["number"]}/reactions?per_page=100')
        counts={k:0 for k in ["+1","heart","rocket","eyes","-1"]}
        for x in react:
            if x.get("content") in counts: counts[x["content"]]+=1
        records.append({"issue_number":i["number"],"title":i["title"],"url":i["html_url"],"area":area,"status":next((x for x in labels if x.startswith("status:")),"status:submitted"),"labels":labels,"state":i["state"],"opened_at":i["created_at"],"reactions":counts,"score":score(counts)})
except Exception as e:
    print("Using existing or empty public data:", e)
write("requests.json",records)
write("votes.json",[{"issue_number":x["issue_number"],"reactions":x["reactions"],"score":x["score"]} for x in records])
write("public-roadmap.json",[x for x in records if any(l in x.get("labels",[]) for l in ["status:approved-public","approved-now"])])
write("approved-now.json",[dict(x, private_packet_status="public-markex-only") for x in records if "approved-now" in x.get("labels",[])])
print("Built public data")
