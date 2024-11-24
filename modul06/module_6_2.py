# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств"

class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # допустимые цвета для окрашивания

    def __init__(self, owner, model, color, engin_power):
        self.owner = owner  # владелец, str
        self.__model = model  # модель, str
        self.__engin_power = engin_power  # мощность двигателя, int
        self.__color = color  # цвет, str

    # возвращает строку: "Модель: <название модели транспорта>"
    def get_model(self):
        return f"Модель: {self.__model}"

    # возвращает строку: "Мощность двигателя: <мощность>"
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engin_power}"

    # возвращает строку: "Цвет: <цвет транспорта>"n
    def get_color(self):
        return f"Цвет: {self.__color}"

    # распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
    # а так же владельца в конце в формате "Владелец: <имя>"
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    # принимает аргумент new_color(str), меняет цвет __color на new_color,
    # если он есть в списке __COLOR_VARIANTS,
    # в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>"
    def set_color(self, new_color):
        evrika = False
        for clr in self.__COLOR_VARIANTS:
            if new_color.upper() == clr.upper():
                evrika = True
                break
        if evrika:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на новый цвет: {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engin_power):
        super().__init__(owner, model, color, engin_power)


if __name__ == '__main__':
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
    # Изначальные свойства
    vehicle1.print_info()
    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'
    # Проверяем что поменялось
    vehicle1.print_info()
