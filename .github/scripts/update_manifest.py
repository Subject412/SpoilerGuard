import json, datetime, sys

version, checksum = sys.argv[1], sys.argv[2]
p = "manifest.json"
d = json.load(open(p))
d[0]["versions"][0].update({
    "version": version,
    "sourceUrl": f"https://github.com/Subject412/SpoilerGuard/releases/download/v{version}/SpoilerGuardLite.zip",
    "checksum": checksum,
    "timestamp": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
})
json.dump(d, open(p, "w"), indent=2)
open(p, "a").write("\n")