from pika import PlainCredentials, BlockingConnection, ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic
from pika.spec import BasicProperties
from app.settings import (
                      RABBITMQ_DEFAULT_HOST, 
                      RABBITMQ_DEFAULT_USER, 
                      RABBITMQ_DEFAULT_PASS, 
                      RABBITMQ_MAIN_QUEUE
                    )


"""
This code follows the basic RabbitMQ tutorial:
https://rabbitmq.com/tutorials/tutorial-one-python.html
"""


def callback(
    channel: BlockingChannel, 
    method: Basic.Deliver, 
    properties: BasicProperties, 
    body: bytes
  ):
  ## Do something with body messages
  print(body)


def receiver():
  credentials = PlainCredentials(RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS)
  connection = BlockingConnection(ConnectionParameters(RABBITMQ_DEFAULT_HOST,
                                                                 credentials=credentials))
  channel = connection.channel()
  channel.queue_declare(RABBITMQ_MAIN_QUEUE)

  # consumer
  channel.basic_consume(
    queue=RABBITMQ_MAIN_QUEUE,
    auto_ack=True,
    on_message_callback=callback
  )

  print('Waiting for new messages. To exit press CTRL+C')
  channel.start_consuming()
