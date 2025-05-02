from google.adk.agents import LoopAgent, ToolAgent
from agents.search_agent import search_agent
from agents.research_agent import research_agent
from agents.email_writer_agent import email_writer_agent
from tools.email_sender import send_email_tool

send_email_agent = ToolAgent(
    name="send_email_agent",
    description="Writes the generated email to a .txt file",
    tool=send_email_tool
)

lead_pipeline = LoopAgent(
    name="lead_pipeline",
    sub_agents=[
        search_agent,
        research_agent,
        email_writer_agent,
        send_email_agent  # ✅ Now this is an Agent, not a raw tool
    ],
    max_iterations=10
)
