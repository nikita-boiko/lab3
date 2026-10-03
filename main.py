from bus.message_bus import MessageBus
from services.order_service import OrderService
from services.inventory_service import InventoryService
from services.notification_service import NotificationService


def main():
    bus = MessageBus()

    order_service = OrderService(bus)

    inventory_service = InventoryService(bus)

    notification_service = NotificationService(bus)

    while True:
        print("\n========== MESSAGE BUS ==========")
        print("1. Создать заказ")
        print("2. Показать склад")
        print("3. Показать уведомления")
        print("4. Показать заказы")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                order_id = int(
                    input("Номер заказа: ")
                )

                product = input(
                    "Название товара: "
                )

                quantity = int(
                    input("Количество: ")
                )

                price = float(
                    input("Цена товара: ")
                )

                order_service.create_order(
                    order_id,
                    product,
                    quantity,
                    price
                )

                print(
                    "Заказ создан и отправлен "
                    "в шину сообщений."
                )

            except ValueError as error:
                print(f"Ошибка: {error}")

        elif choice == "2":
            print("\n========== СКЛАД ==========")

            for product, quantity in (
                inventory_service.stock.items()
            ):
                print(
                    f"{product}: {quantity} шт."
                )

        elif choice == "3":
            print("\n========== УВЕДОМЛЕНИЯ ==========")

            messages = (
                notification_service.get_messages()
            )

            if not messages:
                print("Уведомлений нет.")

            for message in messages:
                print(message)

        elif choice == "4":
            print("\n========== ЗАКАЗЫ ==========")

            orders = order_service.get_orders()

            if not orders:
                print("Заказов нет.")

            for order in orders:
                print(
                    f"№{order.id} | "
                    f"{order.product} | "
                    f"{order.quantity} шт. | "
                    f"{order.total_price():.2f} руб."
                )

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()
