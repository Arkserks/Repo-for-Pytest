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