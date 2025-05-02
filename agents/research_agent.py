from google.adk.agents import LlmAgent
from tools.web_scraper import scrape_website_tool

research_agent = LlmAgent(
    name="research_agent",
    model="litellm/gemini-2.0-flash",
    instruction="""
    For each provided URL, use the scrape_website tool to gather basic information about the company.
    Based on the content, summarize:
    - What the company does
    - Who its likely customers are
    - Any pain points or opportunities your startup could address
    """,
    description="Agent that analyzes websites and produces summarized company info.",
    tools=[scrape_website_tool],
)
