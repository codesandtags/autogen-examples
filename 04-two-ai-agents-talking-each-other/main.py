import asyncio

from autogen_core import AgentId, SingleThreadedAgentRuntime
from autogen_core.models import SystemMessage

from assistant import Assistant
from client import get_model_client
from class_types import (Message, AgentProfile)

def get_system_messages(profile: AgentProfile) -> list[SystemMessage]:
    return [
        SystemMessage(
            content=f"Your name is {profile.name}. You are a {profile.personality}. {profile.mission}"
        )
    ]

async def main() -> None:
    runtime = SingleThreadedAgentRuntime()

    milu = await Assistant.register(
        runtime,
        "milu",
        lambda: Assistant(
            name="Milu",
            model_client=get_model_client(),
            system_messages=get_system_messages(
                AgentProfile(
                    name="Milu",
                    personality="witty and sarcastic",
                    mission="You are specialized in clever wordplay and dry humor."
                )
            )
        ),
    )

    nala = await Assistant.register(
        runtime,
        "nala",
        lambda: Assistant(
            name="Nala",
            model_client=get_model_client("dolphin3"),
            system_messages=get_system_messages(
                AgentProfile(
                    name="Nala",
                    personality="energetic and playful",
                    mission="You love talking about science and teaching spanish."
                )
            )
        ),
    )

    runtime.start()
    await runtime.send_message(
        Message("Nala, tell me something interesting today."),
        recipient=AgentId(nala, "default"),
        sender=AgentId(milu, "default"),
    )
    await runtime.stop_when_idle()

asyncio.run(main())