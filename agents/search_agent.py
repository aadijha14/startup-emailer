from google.adk.agents import LlmAgent
from google.adk.tools import google_search

search_agent = LlmAgent(
    name="search_agent",
    model="gemini-2.0-flash",
    instruction="Given a startup idea, search for relevant companies or people that might be potential customers.",
    description="Agent that uses Google Search to find potential leads.",
    tools=[google_search],
)
