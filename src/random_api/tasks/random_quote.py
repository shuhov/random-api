import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from random_api.common.repository.quotes import get_random_quote

rabbitmq_broker = RabbitmqBroker(url="amqp://user:password@172.17.0.2:5672")
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor(time_limit=6000)
def print_random_quote(q):
    print(get_random_quote(q))
