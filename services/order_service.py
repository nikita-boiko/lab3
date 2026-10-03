from models.order import Order
from events.order_events import OrderCreated
from bus.message_bus import MessageBus


class OrderService:
    """
    Сервис создания заказов.
    Не знает напрямую о других сервисах.
    """

    def __init__(self, bus: MessageBus):
        self.bus = bus
        self.orders = []

    def create_order(
        self,
        order_id: int,
        product: str,
        quantity: int,
        price: float
    ) -> Order:

        if quantity <= 0:
            raise ValueError(
                "Количество должно быть больше нуля."
            )

        if price <= 0:
            raise ValueError(
                "Цена должна быть больше нуля."
            )

        order = Order(
            id=order_id,
            product=product,
            quantity=quantity,
            price=price
        )

        self.orders.append(order)

        event = OrderCreated(
            order_id=order.id,
            product=order.product,
            quantity=order.quantity,
            total_price=order.total_price()
        )

        self.bus.publish(event)

        return order

    def get_orders(self) -> list[Order]:
        return self.orders
