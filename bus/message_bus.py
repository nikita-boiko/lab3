from collections import defaultdict
from typing import Callable


class MessageBus:
    """
    Простая шина сообщений.
    Реализует паттерн Publish/Subscribe.
    """

    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(
        self,
        message_type: type,
        handler: Callable
    ) -> None:
        self.subscribers[message_type].append(handler)

    def publish(self, message) -> None:
        message_type = type(message)

        handlers = self.subscribers.get(
            message_type,
            []
        )

        for handler in handlers:
            handler(message)
