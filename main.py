import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from workflows.lead_pipeline import lead_pipeline
from dotenv import load_dotenv
load_dotenv()

# Constants
APP_NAME = "startup_emailer"
USER_ID = "user_123"
SESSION_ID = "session_001"

async def main():
    # Initialize session service and create a session
    session_service = InMemorySessionService()
    session = session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)

    # Initialize the runner with your lead_pipeline agent
    runner = Runner(agent=lead_pipeline, app_name=APP_NAME, session_service=session_service)

    # Define your startup idea
    idea = "A B2B SaaS platform for automating invoice reconciliation for logistics companies."

    # Create the input content
    content = types.Content(role="user", parts=[types.Part(text=idea)])

    # Run the agent and process the events
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
        if event.content and event.content.parts:
            print(event.content.parts[0].text)

# Execute the main function
if __name__ == "__main__":
    asyncio.run(main())
