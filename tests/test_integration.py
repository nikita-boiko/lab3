from bus.message_bus import MessageBus
from services.order_service import OrderService
from services.inventory_service import InventoryService
from services.notification_service import NotificationService


def test_services_interaction_through_bus():
    bus = MessageBus()

    order_service = OrderService(bus)

    inventory_service = InventoryService(bus)

    notification_service = NotificationService(bus)

    order_service.create_order(
        order_id=1,
        product="Ноутбук",
        quantity=2,
        price=50000
    )

    # Проверяем работу OrderService
    assert len(order_service.get_orders()) == 1

    # Проверяем передачу сообщения
    # в InventoryService
    assert inventory_service.get_stock(
        "Ноутбук"
    ) == 8

    # Проверяем обработку заказа
    assert 1 in inventory_service.processed_orders

    # Проверяем получение сообщения
    # NotificationService
    messages = notification_service.get_messages()

    assert len(messages) == 2

    assert "Создан заказ №1" in messages[0]
    assert "Заказ №1 обработан" in messages[1]
