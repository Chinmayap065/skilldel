def build_prompt(profile, grants):

    return f"""
You are a government startup grant eligibility evaluator.

Startup Profile:
{profile}

Grant Data:
{grants}

IMPORTANT RULES:
- Evaluate each grant only once.
- Return exactly ONE evaluation per grant.
- Do NOT repeat the grant.
- Do NOT provide multiple versions.
- Do NOT re-evaluate.
- Stop after the final decision.
- Do not generate duplicate sections.

STRICT OUTPUT FORMAT (follow exactly once per grant):

### Grant Name: <Grant Name>

**Eligibility Score:** <Percentage>%

**Matched Criteria:**
- <List>

**Qualification Gaps:**
- <List or None>

**Documentation Risks:**
- <List or None>

**Final Decision:** <Eligible / Partially Eligible / Not Eligible>

Do not include explanations outside this structure.
"""