from datetime import datetime

import dramatiq
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from dramatiq.brokers.rabbitmq import RabbitmqBroker


rabbitmq_broker = RabbitmqBroker(url="amqp://user:password@172.17.0.2:5672")
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
def print_current_date():
    print(datetime.now())


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(
        print_current_date.send,
        CronTrigger.from_crontab("* * * * *"),
    )
    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()
