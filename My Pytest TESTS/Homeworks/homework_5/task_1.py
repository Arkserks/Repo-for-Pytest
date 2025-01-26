# Задание 1: Работа со строками и срезами
text = "Python is a powerful programming language"

# Условие 1 Выведите первые 6 символов строки.
first_6_symbols = text[:6]
print(first_6_symbols)

# Условие 2 Выведите последнее слово строки.
index_last_word = text.index("language")
last_word = text[index_last_word:]
last_word2 = text.split()[5]
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