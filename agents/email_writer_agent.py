from google.adk.agents import LlmAgent
from tools.email_sender import send_email_tool

email_writer_agent = LlmAgent(
    name="email_writer_agent",
    model="litellm/gemini-2.0-flash",
    instruction="""
    Based on the company information and our startup's offering, write a personalized cold outreach email.
    
    Include:
    - A friendly greeting
    - A line that shows we understand what they do
    - A brief pitch on how we can help
    - A call to action (e.g., booking a quick call)
    
    Be concise, professional, and not too salesy.
    """,
    description="Generates personalized cold emails using startup value prop and lead info.",
    tools=[send_email_tool],
)
