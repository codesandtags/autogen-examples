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
    }
)


async def main() -> None:
    # Response without using streams
    print(f"Using model: [{model_client._raw_config['model']}]")
    response = await model_client.create([
        UserMessage(
            content="What do you think about human being?",
            source="user"
        )])
    print(response)

    messages = [
        UserMessage(
            content="Write a very short story about a dragon.",
            source="user"
        ),
    ]

    # Create a stream.
    stream = model_client.create_stream(messages=messages)

    # Iterate over the stream and print the responses.
    print("Streamed responses:")
    async for response in stream:  # type: ignore
        if isinstance(response, str):
            # A partial response is a string.
            print(response, flush=True, end="")
        else:
            # The last response is a CreateResult object with the complete message.
            print("\n\n------------\n")
            print("The complete response:", flush=True)
            print(response.content, flush=True)
            print("\n\n------------\n")
            print("The token usage was:", flush=True)
            print(response.usage, flush=True)


asyncio.run(main())