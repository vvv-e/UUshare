# Домашнее задание по теме "Создание исключений"

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin if self.__is_valid_vin(vin) else None
        self.__numbers = numbers if self.__is_valid_numbers(numbers) else None

    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True

    def __is_valid_numbers(self,numbers):
        if not isinstance(numbers, str):
            raise IncorrectVinNumber("Некорректный тип данных для номеров")
        elif len(numbers) != 6:
            raise IncorrectVinNumber("Неверная длина номера")
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


if __name__ == "__main__":
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')
