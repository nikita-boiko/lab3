from dataclasses import dataclass


@dataclass
class Order:
    id: int
    product: str
    quantity: int
    price: float

    def total_price(self) -> float:
        return self.quantity * self.price
