# Задание 3: Работа со списками и строками
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Условие 1 Преобразуйте список в строку, где слова разделены запятой и пробелом.
words_to_str = ', '.join(words)
print(words_to_str)

# Условие 2 Выведите длину каждого слова в списке.
words_len = len(words[0]), len(words[1]), len(words[2]), len(words[3]), len(words[4])
print(words_len) # Не понимаю почему мой ответ отличается

# Условие 4 Выведите строку, где каждое слово начинается с заглавной буквы.
title_text = words_to_str.title()
print(title_text)