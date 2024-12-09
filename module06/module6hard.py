# Дополнительное практическое задание по модулю: "Наследование классов."
from math import pi, sqrt, prod


# родительский
class Figure:
    sides_count = 0

    def __init__(self, color, sides):
        self.filled = None  # закрашенный, bool
        if self.__is_valid_color(color[0], color[1], color[2]):
            self.__color = color  # список цветов, формат RGB
        else:
            self.__color = None
        self.__sides = sides  # список сторон, целые числа

    # Метод возвращает список RGB цветов.
    def get_color(self):
        return [i for i in self.__color]

    # Метод служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой
    # нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and r >= 0 and r <= 255 and isinstance(g, int) and g >= 0
                and g <= 255 and isinstance(b, int) and b >= 0 and b <= 255):
            return True
        else:
            return False

    # Метод  принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно
    # проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Метод служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные
    # числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    def __is_valid_sides(self, *args):
        if isinstance(len, list) and isinstance(self.__sides, list) and len(args) == len(self.__sides):
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
        if isinstance(self.get_sides(), list):
            return sum(self.get_sides())
        else:
            return 0

    # принимает новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.
    def set_sides(self, *new_sides):
        if len(new_sides) == len(self.get_sides()):
            evrika = False
            for i in new_sides:
                if not isinstance(i, int):
                    evrika = True
                    break
            if not evrika:
                self.__sides = [i for i in new_sides]


# круг
class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        if len(args) == Circle.sides_count and isinstance(args[0], int):
            super().__init__(color, [args[0]])
        else:
            super().__init__(color, [1])
        self.__radius = self.get_sides()[0] / (2. * pi)  # радиус

    # переопределена для вычисления радиуса
    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] / (2. * pi)  # радиус

    # возвращает площадь круга (расчет через радиус).
    def get_square(self):
        return pi * self.__radius ** 2

    # возвращает радиус
    def get_radius(self):
        return self.__radius


# треугольник
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        if (len(args) == Triangle.sides_count
                and isinstance(args[0], int) and isinstance(args[1], int) and isinstance(args[2], int)):
            super().__init__(color, [args[i] for i in range(Triangle.sides_count)])
        else:
            super().__init__(color, [1 for i in range(Triangle.sides_count)])

    # площадь треугольника по формуле Герона
    def get_square(self):
        s = sum(self.get_sides(), 0) / 2.
        return sqrt(s * prod([s - i for i in self.get_sides()]))


# куб
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *args):
        if len(args) == 1 and isinstance(args[0], int):
            super().__init__(color, [args[0] for i in range(Cube.sides_count)])
        else:
            super().__init__(color, [1 for i in range(Cube.sides_count)])

    # возвращает объём куба.
    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)
    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())
    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())
    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))
    # Проверка объёма (куба):
    print(cube1.get_volume())

    print("\nпроверка вычислений " + "-" * 25)
    print(f"\nплощадь круга={circle1.get_square()}")
    print(f"радиус круга={circle1.get_radius()}")
    triangle1 = Triangle((200, 200, 100), 2, 3, 4)  # (Цвет, стороны)
    print(f"площадь треугольника={triangle1.get_square()}")
