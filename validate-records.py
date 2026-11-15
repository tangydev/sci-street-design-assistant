"""Check that example design records obey the Section 1 definitions.
Usage: python validate_records.py records/*.json"""
import json, sys

def check_outcome(p):            # met if P>=0.95, not met if P<=0.05
    return "met" if p >= 0.95 else "not_met" if p <= 0.05 else "indeterminate"

def option_status(checks):       # any not_met -> not_met; else any indet -> indet; else met
    s = {c["outcome"] for c in checks}
    return "not_met" if "not_met" in s else "indeterminate" if "indeterminate" in s else "met"

def validate(rec):
    errs = []
    w = rec["measured_width_m"]["median_m"]
    statuses = {}
    for o in rec["options"]:
        fixed = sum(e["width_m"] for e in o["elements"] if not e.get("derived"))
        for c in o["checks"]:
            if check_outcome(c["p_meet"]) != c["outcome"]:
                errs.append(f'{o["id"]}/{c["rule_id"]}@{c["station_m"]}: p={c["p_meet"]} but outcome={c["outcome"]}')
            if not c["p05_m"] <= c["median_m"] <= c["p95_m"]:
                errs.append(f'{o["id"]}/{c["rule_id"]}: band not ordered')
            if c["element"] == "bike_lane" and c["station_m"] == 0 and abs(fixed + c["median_m"] - w) > 0.02:
                errs.append(f'{o["id"]}: widths sum to {fixed + c["median_m"]:.2f}, measured {w}')
        statuses[o["id"]] = option_status(o["checks"])
    v = set(statuses.values())
    expected = "feasible" if "met" in v else "unresolved" if "indeterminate" in v else "infeasible"
    if expected != rec["outcome"]:
        errs.append(f'outcome {rec["outcome"]} but options give {expected} {statuses}')
    rid = rec["recommended_id"]
    if rid is not None and statuses.get(rid) != "met":
        errs.append(f"recommended option {rid} is not fully met")
    return errs

ok = True
for path in sys.argv[1:]:
    errs = validate(json.load(open(path)))
    print(("OK   " if not errs else "FAIL ") + path)
    for e in errs: print("     " + e)
    ok &= not errs
sys.exit(0 if ok else 1)