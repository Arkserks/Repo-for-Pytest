# import csv
#
#
# with open('data.csv', newline='') as csv_file:
#     file_data = csv.reader(csv_file)
#     data = []
#     for row in file_data:
#         data.append(row)
#
#
#
# for row in data:
#     city, name, age, color = row
#     print(f'City: {city}, name: {name}, age: {age}, color: {color}')

import csv

with open('data.csv', newline='') as csv_file:
    # Используем DictReader для автоматического назначения заголовков как ключей
    file_data = csv.DictReader(csv_file)

    # Чтение данных и вывод по ключам
    for row in file_data:
        city = row['City']
        name = row['Name']
        age = row['Age']
        color = row['Color']
        print(f'City: {city}, name: {name}, age: {age}, color: {color}')
