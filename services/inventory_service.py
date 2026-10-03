from events.order_events import (
    OrderCreated,
    OrderProcessed
)
from bus.message_bus import MessageBus


class InventoryService:
    """
    Сервис управления складом.
    """

    def __init__(self, bus: MessageBus):
        self.bus = bus

        self.stock = {
            "Ноутбук": 10,
            "Смартфон": 20,
            "Наушники": 30,
            "Клавиатура": 15
        }

        self.processed_orders = []

        bus.subscribe(
            OrderCreated,
            self.process_order
        )

    def process_order(
        self,
        event: OrderCreated
    ) -> None:

        current_stock = self.stock.get(
            event.product,
            0
        )

        if current_stock < event.quantity:
            return

        self.stock[event.product] = (
            current_stock - event.quantity
        )

        self.processed_orders.append(
            event.order_id
        )

        self.bus.publish(
            OrderProcessed(
                order_id=event.order_id,
                product=event.product,
                quantity=event.quantity
            )
        )

    def get_stock(self, product: str) -> int:
        return self.stock.get(product, 0)
