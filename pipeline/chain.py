from retriever.grant_retriever import retrieve
from llm.groq_llm import generate_response
from pipeline.prompt_template import build_prompt
from pipeline.output_parser import format_output
from langsmith import traceable

@traceable(name="Grant Eligibility Chain")
def run_chain(profile):

    # input → retriever
    grants = retrieve(profile)

    if not grants:
        return "No matching grants found."

    # retriever → prompt
    prompt = build_prompt(profile, grants)

    # prompt → llm
    raw_output = generate_response(prompt)

    # llm → output
    final_output = format_output(raw_output)

    return final_output