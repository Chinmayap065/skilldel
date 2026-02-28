from database.db import fetch_grants
from langsmith import traceable

@traceable(name="Grant Retriever")
def retrieve(profile):

    grants = fetch_grants()
    matched = []

    for g in grants:
        _, name, sector, min_rev, max_rev, stage, dpiit, state, desc, docs = g

        # Sector check
        if sector != "Any" and sector.lower() != profile["sector"].lower():
            continue

        # Revenue check
        if not (min_rev <= profile["revenue"] <= max_rev):
            continue

        # Stage check
        if stage.lower() != profile["stage"].lower():
            continue

        # DPIIT check
        if dpiit == 1 and profile["dpiit"] == "No":
            continue

        # State check (handle "Any")
        if state.lower() != "any" and state.lower() != profile["state"].lower():
            continue

        matched.append({
            "name": name,
            "sector": sector,
            "min_revenue": min_rev,
            "max_revenue": max_rev,
            "stage": stage,
            "dpiit_required": dpiit,
            "state": state,
            "description": desc,
            "documents": docs
        })

    return matched