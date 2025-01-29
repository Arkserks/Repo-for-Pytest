#Цикл for (for loop)

names = ['Jone', 'Sarah', 'Bob', 'Saymon', 'Jenna']

for name in names:
    if name.startswith('J'):
        print('Mr.', end=' ')
    print(name)


# Для словарей
persons = {'Jone': 123, 'Sarah': 567, 'Bob': 888, 'Saymon': 999, 'Jenna': 112}

for person in persons:
    print(f"Возраст {person} примерно {persons[person]}")

# Еще вариант со словарем
persons = {'Jone': 123, 'Sarah': 567, 'Bob': 888, 'Saymon': 999, 'Jenna': 112}
for name, age in persons.items():
    print(f"{name}: {age}")

