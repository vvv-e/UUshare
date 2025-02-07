# Задача "История строительства"

class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if args[0] in cls.houses_history:
            print(f'{args[0]} уже есть в истории, объект не создан')
        else:
            cls.houses_history.append(args[0])
            return super().__new__(cls)

    def __del__(self):
        print(f'{self.name} снесен, но останется в истории')

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return "Название: " + self.name + ", кол-во этажей: " + str(self.number_of_floors)

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('операнд не является объектом класса ' + self.__class__.__name__)
            return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('операнд не является объектом класса ' + self.__class__.__name__)
            return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('операнд не является объектом класса ' + self.__class__.__name__)
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            print('операнд не является объектом класса ' + self.__class__.__name__)
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('операнд не является объектом класса ' + self.__class__.__name__)
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            print('операнд не является объектом класса ' + self.__class__.__name__)
            return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print('операнд не является объектом класса int')
            return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    # Удаление объектов
    del h2
    del h3
    print(House.houses_history)
