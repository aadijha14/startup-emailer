from google.adk.agents import LlmAgent
from google.adk.tools import google_search

search_agent = LlmAgent(
    name="search_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a lead generation assistant. 
    Given a startup idea, use Google Search to find potential customers — companies or people. 
    For each result, return the following:
    - Name
    - 1-line description (if available)
    - URL

    Format each entry like this:
    [
    {
        "name": "Acme Corp",
        "description": "Enterprise SaaS platform for HR automation",
        "url": "https://acmecorp.com"
    },
    ...
    ]
    Return only the list — no extra commentary.
    """.strip(),
    description="Agent that uses Google Search to find potential leads.",
    tools=[google_search],
)
