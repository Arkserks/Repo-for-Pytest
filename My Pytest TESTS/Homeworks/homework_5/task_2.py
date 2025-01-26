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
data_count = len(data_upper.split())
print(data_count) # Не понимаю почему мой ответ отличается

!!!!!!!!!!!