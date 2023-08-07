from app.settings import (
    RABBITMQ_DEFAULT_HOST,
    RABBITMQ_DEFAULT_USER,
    RABBITMQ_DEFAULT_PASS,
    RABBITMQ_SEND_QUEUE,
)
import pika

"""
This code follows the basic RabbitMQ tutorial:
https://rabbitmq.com/tutorials/tutorial-one-python.html
"""

try:
    # set connection credentials
    credentials = pika.PlainCredentials(RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS)

    # create chanel and queue
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(RABBITMQ_DEFAULT_HOST, credentials=credentials)
    )
    channel = connection.channel()
    channel.queue_declare(RABBITMQ_SEND_QUEUE)

    # publish message
    message = "hello guilherme"
    channel.basic_publish(exchange="", routing_key=RABBITMQ_SEND_QUEUE, body=message)

    # close connection
    connection.close()
except Exception as e:
    print(e)
