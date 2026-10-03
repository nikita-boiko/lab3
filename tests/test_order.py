import pytest

from bus.message_bus import MessageBus
from services.order_service import OrderService


def test_create_order():
    bus = MessageBus()

    service = OrderService(bus)

    order = service.create_order(
        order_id=1,
        product="Ноутбук",
        quantity=2,
        price=50000
    )

    assert order.id == 1
    assert order.product == "Ноутбук"
    assert order.quantity == 2
    assert order.total_price() == 100000


def test_invalid_quantity():
    bus = MessageBus()

    service = OrderService(bus)

    with pytest.raises(ValueError):
        service.create_order(
            1,
            "Ноутбук",
            0,
            50000
        )


def test_invalid_price():
    bus = MessageBus()

    service = OrderService(bus)

    with pytest.raises(ValueError):
        service.create_order(
            1,
            "Ноутбук",
            1,
            0
        )
