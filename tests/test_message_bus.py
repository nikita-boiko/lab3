from bus.message_bus import MessageBus


class TestMessage:
    pass


def test_subscribe_and_publish():
    bus = MessageBus()

    received = []

    def handler(message):
        received.append(message)

    bus.subscribe(
        TestMessage,
        handler
    )

    message = TestMessage()

    bus.publish(message)

    assert len(received) == 1
    assert received[0] is message


def test_multiple_subscribers():
    bus = MessageBus()

    received_1 = []
    received_2 = []

    bus.subscribe(
        TestMessage,
        lambda message: received_1.append(message)
    )

    bus.subscribe(
        TestMessage,
        lambda message: received_2.append(message)
    )

    bus.publish(TestMessage())

    assert len(received_1) == 1
    assert len(received_2) == 1
