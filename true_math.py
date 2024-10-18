# к заданию модуль_4_1

from math import inf

def divide(first, second):
    try:
        result = first / second
    except ZeroDivisionError:
        return inf
    else:
        return result
