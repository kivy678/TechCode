#-*- coding: utf-8 -*-

##############################################################################

import pika
from settings import *

##############################################################################


def callback(ch, method, properties, body):
    print(f"[x] Received {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


credentials = pika.PlainCredentials(PIKA_ID, PIKA_PASSWD)

connection = pika.BlockingConnection(pika.ConnectionParameters(
									host=PIKA_HOST, credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue=CHANNEL_NAME,
						durable=True)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=CHANNEL_NAME,
						on_message_callback=callback)

channel.start_consuming()
