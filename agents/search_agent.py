from google.adk.agents import Agent  # or use LlmAgent if available
from google.adk.tools import google_search  # ADK's built-in tool for Gemini 2

# Defining agent
search_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",
    instruction="Given a startup idea, search for relevant companies or people that might be potential customers.",
    description="Agent that uses Google Search to find potential leads.",
    tools=[google_search],
)