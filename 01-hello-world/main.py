import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
)

async def main() -> None:
    agent = AssistantAgent("assistant", model_client)
    task = "Say a short message to the world in Spanish."
    await Console((agent.run_stream(task=task)))

asyncio.run(main())