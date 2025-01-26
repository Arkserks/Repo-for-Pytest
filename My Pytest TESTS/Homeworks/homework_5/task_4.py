# Задание 4: Форматирование строк
name = "Alice"
age = 30
city = "Wonderland"

# Условие 1 Используя метод format(), создайте строку:
# "My name is Alice, I am 30 years old, and I live in Wonderland."
new_str_1 = "My name is {}, I am {} years old, and I live in {}".format(name, age, city)
print(new_str_1)
# Условие 2 Используя f-строку, создайте строку:
# "Alice is 30 years old and lives in Wonderland."
new_str_2 = f"{name} is {age} years old and lives in {city}"
print(new_str_2)
# Условие 3 Используя f-строку, создайте строку, где возраст увеличен на 5 лет:
# "In 5 years, Alice will be 35 years old."
new_str_3 = f"In 5 years, {name} will be {age + 5} years old"
print(new_str_3)