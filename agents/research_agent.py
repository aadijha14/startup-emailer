from google.adk.agents import LlmAgent
from tools.web_scraper import scrape_website_tool

research_agent = LlmAgent(
    name="research_agent",
    model="gemini-2.0-flash",
    instruction="""
    For each provided company URL, use the scrape_website tool to gather full website content, including all subpages such as About, Contact, Services, etc.

    Based on the scraped content:
    - Summarize what the company does
    - Identify its likely customer segments
    - Highlight pain points or inefficiencies that our startup could solve
    - If any email addresses or names/titles of relevant people (e.g. logistics, finance, operations) are found, extract and list them
    """,
    description="Agent that deeply analyzes websites to extract company summaries, opportunities, and potential leads.",
    tools=[scrape_website_tool],
)
