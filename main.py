from app.publisher.publisher import RabbitMQPublisher
from json import dumps

if __name__ == "__main__":
  try:
    publisher = RabbitMQPublisher()
    publisher.publish_message(dumps([i for i in range(10)]))
  except KeyboardInterrupt:
    print('Interrupted')