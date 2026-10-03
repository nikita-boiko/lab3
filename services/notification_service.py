from events.order_events import (
    OrderCreated,
    OrderProcessed
)
from bus.message_bus import MessageBus


class NotificationService:
    """
    Сервис уведомлений.
    """

    def __init__(self, bus: MessageBus):
        self.messages = []

        bus.subscribe(
            OrderCreated,
            self.order_created
        )

        bus.subscribe(
            OrderProcessed,
            self.order_processed
        )

    def order_created(
        self,
        event: OrderCreated
    ) -> None:

        message = (
            f"Создан заказ №{event.order_id}: "
            f"{event.product}, "
            f"количество {event.quantity}, "
            f"стоимость {event.total_price:.2f} руб."
        )

        self.messages.append(message)

    def order_processed(
        self,
        event: OrderProcessed
    ) -> None:

        message = (
            f"Заказ №{event.order_id} обработан. "
            f"Товар: {event.product}, "
            f"количество: {event.quantity}."
        )

        self.messages.append(message)

    def get_messages(self) -> list[str]:
        return self.messages
