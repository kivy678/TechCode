#-*- coding: utf-8 -*-

##############################################################################

import pika

try: import simplejson as json
except ImportError: import json

from settings import *

##############################################################################


def pyListToJson(pyList):
	return json.dumps(pyList)

message = pyListToJson(['test', 'hello world'])
credentials = pika.PlainCredentials(PIKA_ID, PIKA_PASSWD)

connection = pika.BlockingConnection(pika.ConnectionParameters(
									host=PIKA_HOST, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue=CHANNEL_NAME, durable=True)
channel.basic_publish(exchange='',
                      routing_key=CHANNEL_NAME,
                      body=message,
                      properties=pika.BasicProperties(
                         		delivery_mode = 2,
                      ))

connection.close()
