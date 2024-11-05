# к заданию модуль_4_1

def divide(first, second):
    try:
        result = first / second
    except ZeroDivisionError:
        return "Ошибка"
    else:
        return result
