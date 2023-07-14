from app.settings import(
                          RABBITMQ_DEFAULT_HOST, 
                          RABBITMQ_DEFAULT_USER, 
                          RABBITMQ_DEFAULT_PASS, 
                          RABBITMQ_MAIN_QUEUE
                        )
from pika import BlockingConnection, ConnectionParameters, PlainCredentials


class RabbitMQPublisher:
  def __init__(self, queue_name: str = RABBITMQ_MAIN_QUEUE) -> None:
    self.credentials = PlainCredentials(RABBITMQ_DEFAULT_USER, RABBITMQ_DEFAULT_PASS)
    self.connection = BlockingConnection(ConnectionParameters(RABBITMQ_DEFAULT_HOST,credentials=self.credentials))
    self.channel = self.connection.channel()
    self.queue_name = queue_name
    self.channel.queue_declare(self.queue_name)

  def publish_message(self, message: str | bytes):
    self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=message)
    self.connection.close()

from json import dumps
p = RabbitMQPublisher()
message = {'guilherme': 'boiola'}
p.publish_message(dumps(message))
