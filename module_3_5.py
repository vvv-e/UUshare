# Самостоятельная работа по уроку "Рекурсия".

def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0:1])
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) <= 1:
        return int(str_number[0:1])

result = get_multiplied_digits(40203)
print(result)
