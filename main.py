from app.publisher.publisher import RabbitMQPublisher
from json import dumps

l = ['B07H6DPQ6B', 'B07N1G1THD', 'B09VZ8YC6G', 'B09VCPNY1T', 'B096QY7ZQQ', 'B09WVLVWGY', 'B09NQ8WQ5Q', 'B095HM612T', 'B09C22CQQV', 'B09VP8S3PN', 'B0BZQNPM6D', 'B09X3492XJ', 'B09BZNTVQC', 'B0C11HL98H', 'B08TTLMKXG', 'B0BZ16FM6X']

if __name__ == "__main__":
  try:
    publisher = RabbitMQPublisher()
    publisher.publish_message(dumps(l))
  except KeyboardInterrupt:
    print('Interrupted')
