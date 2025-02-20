from db_connect import execute_query

# SQL-запрос для выборки данных
query = "SELECT * FROM flights WHERE id = 23"

# Выполняем запрос и выводим результат
result = execute_query(query)
if result:
    for row in result:
        print(row)
