import json

def task() -> float:
    #чтение данных из файла input.json
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    #проход по каждому словарю в списке
    for item in data:
        if 'score' in item and 'weight' in item:
            total_sum += item['score'] * item['weight']
    return round(total_sum, 3)

print(task())
