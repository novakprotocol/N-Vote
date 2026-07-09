import json, os, urllib.request
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]; data=root/"data"; repo=os.getenv("GITHUB_REPOSITORY","novakprotocol/N-Vote")
boundary="Public issues and reactions are public signals only. Owner approval is required before private work."
kinds=["app","web app","game","overlay","docs","other"]
areas=["application-request","n-suite","overlay","n-idea","n-g-games","n-g-chess","n-g-pegsolitaire","local-bridge","docs","other"]
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def write(name,records):
    (data/name).write_text(json.dumps({"schema":"n-vote.public-data.v1."+name.replace(".json","").replace("-","_"),"generated_at":now(),"source_repo":"novakprotocol/N-Vote","public_private_boundary":boundary,"records":records},indent=2,sort_keys=True)+"\n",encoding="utf-8")
def load(name):
    try: return json.loads((data/name).read_text(encoding="utf-8")).get("records",[])
    except Exception: return []
def api(path):
    h={"Accept":"application/vnd.github+json","User-Agent":"n-vote"}; tok=os.getenv("GITHUB_TOKEN")
    if tok: h["Authorization"]="Bearer "+tok
    with urllib.request.urlopen(urllib.request.Request("https://api.github.com/repos/"+repo+path,headers=h),timeout=30) as r: return json.load(r)
def score(r): return r.get("+1",0)+2*r.get("heart",0)+3*r.get("rocket",0)+.5*r.get("eyes",0)-r.get("-1",0)
def area(labels):
    xs=[x.split(":",1)[1] for x in labels if x.startswith("area:")]
    if "application-request" in xs: return "application-request"
    for x in xs:
        if x in areas and x!="public-intake": return x
    return xs[0] if xs else "other"
def req_type(labels,a): return "application-request" if "type:application-request" in labels or a=="application-request" else ("feature" if "type:feature" in labels else "request")
def reacts(n):
    out={k:0 for k in ["+1","heart","rocket","eyes","-1"]}
    for x in api(f"/issues/{n}/reactions?per_page=100"):
        if x.get("content") in out: out[x["content"]]+=1
    return out
records=[]
try:
    for i in api("/issues?state=all&per_page=100"):
        if "pull_request" in i: continue
        labels=[x["name"] for x in i.get("labels",[])]
        a=area(labels); r=reacts(i["number"])
        rec={"area":a,"issue_number":i["number"],"title":i["title"],"url":i["html_url"],"status":next((x for x in labels if x.startswith("status:")),"status:submitted"),"labels":labels,"state":i["state"],"opened_at":i["created_at"],"reactions":r,"score":score(r),"request_type":req_type(labels,a),"public_routing":{"friday_top5":True,"approved_now_requires_owner_approval":True}}
        if a=="application-request": rec["request_kinds_supported"]=kinds
        records.append(rec)
except Exception as e:
    print("Using existing public data:",e); records=load("requests.json")
write("requests.json",records)
write("votes.json",[{"issue_number":x["issue_number"],"reactions":x.get("reactions",{}),"score":x.get("score",0)} for x in records])
write("public-roadmap.json",[x for x in records if any(l in x.get("labels",[]) for l in ["status:approved-public","approved-now"])])
write("approved-now.json",[dict(x,private_work_status="owner-approval-required") for x in records if "approved-now" in x.get("labels",[])])
base={x.get("slug"):x for x in load("areas.json") if x.get("slug")}
defaults={"application-request":{"slug":"application-request","display_name":"Application Requests","description":"Public-safe requests for apps, web apps, games, overlay features, docs, or other app-like ideas.","request_kinds":kinds}}
for a in areas: base.setdefault(a,defaults.get(a,{"slug":a,"display_name":a,"description":""}))
active=[x for x in records if x.get("state","open")=="open"]
for a,x in base.items(): x["open_request_count"]=len([r for r in active if r.get("area")==a]); x["top_request_count"]=min(5,x["open_request_count"])
write("areas.json",[base[a] for a in areas if a in base]+[x for a,x in sorted(base.items()) if a not in areas])
print("Built public data")
