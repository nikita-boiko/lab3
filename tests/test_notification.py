from bus.message_bus import MessageBus
from events.order_events import (
    OrderCreated,
    OrderProcessed
)
from services.notification_service import (
    NotificationService
)


def test_order_created_notification():
    bus = MessageBus()

    service = NotificationService(bus)

    event = OrderCreated(
        order_id=1,
        product="Ноутбук",
        quantity=2,
        total_price=100000
    )

    bus.publish(event)

    messages = service.get_messages()

    assert len(messages) == 1
    assert "Создан заказ №1" in messages[0]


def test_order_processed_notification():
    bus = MessageBus()

    service = NotificationService(bus)

    event = OrderProcessed(
        order_id=1,
        product="Ноутбук",
        quantity=2
    )

    bus.publish(event)

    messages = service.get_messages()

    assert len(messages) == 1
    assert "Заказ №1 обработан" in messages[0]
