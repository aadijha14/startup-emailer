from google.adk.agents import LoopAgent
from agents.search_agent import search_agent
from agents.research_agent import research_agent
from agents.email_writer_agent import email_writer_agent  # Now includes send_email_tool

lead_pipeline = LoopAgent(
    name="lead_pipeline",
    sub_agents=[
        search_agent,
        research_agent,
        email_writer_agent  # This agent now internally handles writing the email to file
    ],
    max_iterations=50
)
