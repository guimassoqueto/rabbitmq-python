from app.publisher.publisher import RabbitMQPublisher
from app.csv.ids_to_list import ids_to_list
from app.delete_file.delete_file import delete_file
from json import dumps
from sys import argv

def template_for() -> str:
  template_for = input("[T]THUNDER [K]KADEC: ")
  while True:
    template_for = template_for.lower()

    if template_for == 't':
      thunder_options = input("[S]STORY [FF]FEED FULL [FQ]FEED QUARTER: ").lower()
      if thunder_options == 's': return 'ts'
      if thunder_options == 'ff': return 'tff'
      if thunder_options == 'fq': return 'tfq'

    if template_for == 'k': return 'k'
    
    print('INVALID OPTION. THE OPTIONS ARE T OR K.\n')
    template_for = input("[T]THUNDER [K]KADEC: ")


if __name__ == "__main__":
  filename = 'data.csv'
  try:
    option = template_for()
    l = { option: ids_to_list(filename) }

    publisher = RabbitMQPublisher()
    publisher.publish_message(dumps(l))
    delete_file(filename)
  except Exception as e:
    print(e)
