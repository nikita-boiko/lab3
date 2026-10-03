from dataclasses import dataclass


@dataclass
class OrderCreated:
    order_id: int
    product: str
    quantity: int
    total_price: float


@dataclass
class OrderProcessed:
    order_id: int
    product: str
    quantity: int
