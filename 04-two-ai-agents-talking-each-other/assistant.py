from dataclasses import dataclass
from autogen_core import (
    MessageContext,
    RoutedAgent,
    default_subscription,
    message_handler,
    DefaultTopicId
)
from autogen_core.model_context import BufferedChatCompletionContext
from autogen_core.models import (
    AssistantMessage,
    ChatCompletionClient,
    SystemMessage,
    UserMessage,
)
from class_types import Message

@default_subscription
class Assistant(RoutedAgent):
    def __init__(self, name: str, model_client: ChatCompletionClient, system_messages: list[SystemMessage]) -> None:
        super().__init__("An assistant agent.")
        self._model_client = model_client
        self.name = name
        self.count = 0
        self._system_messages = system_messages
        self._model_context = BufferedChatCompletionContext(buffer_size=5)

    @message_handler
    async def handle_message(self, message: Message, ctx: MessageContext) -> None:
        self.count += 1
        await self._model_context.add_message(UserMessage(content=message.content, source="user"))
        result = await self._model_client.create(self._system_messages + await self._model_context.get_messages())

        print(f"\n🤖 {self.name}: {message.content}")

        if "I need to go".lower() in message.content.lower() or self.count > 10:
            return

        await self._model_context.add_message(AssistantMessage(content=result.content, source="assistant"))  # type: ignore
        await self.publish_message(Message(content=result.content), DefaultTopicId())  # type: ignore