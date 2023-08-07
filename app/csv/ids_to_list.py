from typing import List
from csv import DictReader

def ids_to_list(csv_file: str) -> List[str]:
  pid_list = []
  with open(csv_file, 'r', encoding='utf-8') as f:
    reader = DictReader(f, delimiter=',')
    for row in reader:
      pid_list.append(row['id'].split('/')[-1])
  return pid_list