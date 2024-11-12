# Дополнительное практическое задание по модулю: "Наследование классов."
from math import pi

# родительский
class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.filled = None  # закрашенный, bool
        if self.__is_valid_color():
            self.__color = color  # список цветов, формат RGB
        else:
            self.__color = None
        self.__sides = sides  # список сторон, целые числа

    # Метод возвращает список RGB цветов.
    def get_color(self):
        return self.__color

    # Метод служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой
    # нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and r >= 0 and r <= 255
                and isinstance(g, int) and g >= 0 and g <= 255
                and isinstance(b, int) and b >= 0 and b <= 255):
            return True
        else:
            return False

    # Метод  принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно
    # проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    # Метод служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные
    # числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    def __is_valid_sides(self, *args):
        if isinstance(len, list) and isinstance(self.__sides, set) and len(args) == len(self.__sides):
            evrika = False
            for i in args:
                if not isinstance(r, int) or (isinstance(r, int) and r <= 0):
                    evrika = True
                    break
            if not evrika:
                return True
        return False

    # Метод должен возвращать значение атрибута __sides.
    def get_sides(self):
        return self.__sides

    # возвращает периметр фигуры.
    def __len__(self):
        pass

    # принимает новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        pass


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        if len(args) == 1 and isinstance(args[0], int):
            super().__init__(color, [args[0]])
        else:
            super().__init__(color, [1])
        __radius = 1 / ( 2* pi)  # радиус

    # возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
    def get_square(self):
        pass


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        pass


class Cube(Figure):
    sides_count = 12

    # возвращает объём куба.
    def get_volume(self):
        pass
