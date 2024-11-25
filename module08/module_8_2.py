# Домашнее задание по теме "Try и Except"


def personal_sum(numbers):
    incorrect_data = 0
    sum_ = 0.
    for d in numbers:
        try:
            sum_ += d
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {d}')
            incorrect_data += 1
    return sum_, incorrect_data


# Среднее арифметическое - сумма всех данных делённая на их количество.
def calculate_average(numbers):
    try:
        sum_inc_data = personal_sum(numbers)
        avg = sum_inc_data[0] / (len(numbers) - sum_inc_data[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    return avg


if __name__ == "__main__":
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
