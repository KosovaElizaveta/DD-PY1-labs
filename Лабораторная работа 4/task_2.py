
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    #считать содержимое csv файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        #использовать DictReader для чтения содержимого csv файла
        reader = csv.DictReader(csv_file)
        #преобразовать строки в список словарей
        data = [OrderedDict(row) for row in reader]

    #сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    #проверка
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")


