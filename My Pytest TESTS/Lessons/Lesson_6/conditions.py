# Функция которая запрашивает на ввод номер и возвращает буквенное значение. В случае ошибки выводится ошибка пользователю. Работает бесконечно

def check_number():
    user_input = input('Your number: ')

    if user_input.isnumeric():
        user_input = int(user_input)
        if user_input == 1:
            print('One')
            check_number()
        elif user_input == 2:
            print('Two')
            check_number()
        else:
            print('Too much')
            check_number()
    else:
        print('Enter a number plese')
        check_number()


check_number()
