# Задание 1: Работа со строками и срезами
from os import pread

text = "Python is a powerful programming language"
# Условие 1 Выведите первые 6 символов строки.
first_6_symbols = text[:6]
print(first_6_symbols)
# Условие 2 Выведите последнее слово строки.
index_last_word = text.index("language")
last_word = text[index_last_word:]
last_word2 = text.startswith('language')
print(last_word)
print(last_word2) # Не понимаю почему не работает
# Условие 3 Выведите строку в обратном порядке.
revert_str = text[-1::-1]
print(revert_str)
# Условие 4 Выведите каждое второе слово строки (начиная с первого)
words = text.split()
result = words[::2]
result_finish = ' '.join(result)
print(result_finish)

# Задание 2: Методы строк
data = "  Some text with extra spaces and, some, commas  "
# Условие 1 Удалите лишние пробелы в начале и конце строки.
data_strip = data.strip()
print(data_strip)
# Условие 2 Замените все запятые на точки.
data_dot_replace = data_strip.replace(",", ".")
print(data_dot_replace)
# Условие 3 Переведите строку в верхний регистр.
data_upper = data_dot_replace.upper()
print(data_upper)
# Условие 4 Подсчитайте количество слов в строке (разделитель — пробел).
data_count = data_upper.count(' ')
print(data_count) # Не понимаю почему мой ответ отличается

# Задание 3: Работа со списками и строками
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Условие 1 Преобразуйте список в строку, где слова разделены запятой и пробелом.
words_to_str = ', '.join(words)
print(words_to_str)
# Условие 2 Выведите длину каждого слова в списке.
words_len = len(words[0]), len(words[1]), len(words[2]), len(words[3]), len(words[4])
print(words_len) # Не понимаю почему мой ответ отличается
# Условие 3 Создайте новый список, содержащий только слова, длина которых больше 5 символов.
# не понимаю как делать.
# Условие 4 Выведите строку, где каждое слово начинается с заглавной буквы.
title_text = words_to_str.title()
print(title_text)

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

# Задание 5: Работа с вложенными списками и строками
data = [
    ["apple", "banana", "cherry"],
    ["date", "elderberry", "fig"],
    ["grape", "honeydew", "kiwi"]
]

# Условие 1 Преобразуйте каждый внутренний список в строку, где элементы разделены запятой и пробелом.
a_str, b_str, c_str = ', '.join(data[0]), ', '.join(data[1]), ', '.join(data[2]),
print(a_str)
print(b_str)
print(c_str)
# Условие 2 Создайте новый список, содержащий только первые элементы каждого внутреннего списка.
a_str_list = a_str.split(",")
b_str_list = b_str.split(",")
c_str_list = c_str.split(",")
new_list = [a_str_list[0], b_str_list[0], c_str_list[0]]
print(new_list)
# Условие 3 Объедините все строки из пункта 1 в одну строку, разделяя их символом ;.
sum_str = a_str + b_str + c_str
sum_str_replace = sum_str.replace(",", ";")
print(sum_str_replace)
# Условие 4 Выведите строку, где все фрукты написаны в верхнем регистре.
upper_str = sum_str.upper()
print(upper_str) # Не понимаю почему в твоем примере вывода есть ;

