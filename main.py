from app.publisher.publisher import RabbitMQPublisher
from app.csv.ids_to_list import ids_to_list
from app.delete_file.delete_file import delete_file
from json import dumps
from sys import argv

def template_for() -> int:
  template_for = input("[T]THUNDER [K]KADEC: ")
  while True:
    template_for = template_for.lower()
    if template_for == 't': return 1
    if template_for == 'k': return 2
    
    print('INVALID OPTION. THE OPTIONS ARE T OR K.\n')
    template_for = input("[T]THUNDER [K]KADEC: ")


if __name__ == "__main__":
  filename = 'data.csv'
  try:
    option = template_for()

    if option == 1: 
      l = {"thunder": ids_to_list(filename)}
    else:
      l = {"kadec": ids_to_list(filename)}

    print(l)

    publisher = RabbitMQPublisher()
    publisher.publish_message(dumps(l))
    delete_file(filename)
  except Exception as e:
    print(e)
