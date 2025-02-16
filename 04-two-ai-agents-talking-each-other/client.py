from autogen_ext.models.openai import OpenAIChatCompletionClient

def get_model_client(model = "llama2-uncensored") -> OpenAIChatCompletionClient:  # type: ignore
    "Mimic OpenAI API using Local LLM Server."
    print(f"Creating a new client using model: [{model}]")

    return OpenAIChatCompletionClient(
        model=model,
        api_key="NotRequiredSinceWeAreLocal",
        base_url="http://localhost:11434/v1",
        model_capabilities={
            "json_output": False,
            "vision": False,
            "function_calling": True,
        },
    )