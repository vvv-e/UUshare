# Самостоятельная работа по уроку "Рекурсия".
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.

def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0:1])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number[0:1]) if int(str_number[0:1]) > 1 else 1

if __name__ == '__main__':
    result = get_multiplied_digits(40203)
    print(result)
    result = get_multiplied_digits(420)
    print(result)
