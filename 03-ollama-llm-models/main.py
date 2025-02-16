import asyncio
from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient


model_client = OpenAIChatCompletionClient(
    # Add your local model here. (run ollama list to see your models)
    model="llama2-uncensored",
    base_url="http://localhost:11434/v1",
    api_key="placeholder",
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": False,
        "family": "unknown",
    },
)


async def main() -> None:
    print(f"Using model: [{model_client._raw_config['model']}]")
    response = await model_client.create([
        UserMessage(
            content="What do you think about human being?",
            source="user"
        )])
    print(response)


asyncio.run(main())