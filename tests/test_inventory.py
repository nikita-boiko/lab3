from bus.message_bus import MessageBus
from events.order_events import OrderCreated
from services.inventory_service import InventoryService


def test_inventory_processes_order():
    bus = MessageBus()

    inventory = InventoryService(bus)

    event = OrderCreated(
        order_id=1,
        product="Ноутбук",
        quantity=2,
        total_price=100000
    )

    bus.publish(event)

    assert inventory.get_stock("Ноутбук") == 8
    assert 1 in inventory.processed_orders


def test_inventory_does_not_process_excess():
    bus = MessageBus()

    inventory = InventoryService(bus)

    event = OrderCreated(
        order_id=1,
        product="Ноутбук",
        quantity=100,
        total_price=5000000
    )

    bus.publish(event)

    assert inventory.get_stock("Ноутбук") == 10
    assert 1 not in inventory.processed_orders
