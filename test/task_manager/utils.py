from dramatiq.brokers.stub import StubBroker


def get_broker():
    broker = StubBroker()
    broker.emit_after("process_boot")
    broker.declare_queue("default")
    return broker


broker = get_broker()
