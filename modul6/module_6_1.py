# Домашнее задание по теме "Зачем нужно наследование"

class Animal:
    """
    Животное.
    атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
    """

    def __init__(self):
        print("init A")
        self.alive = True
        self.fed = False
        self.name = None

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    """
    Растение.
    edible = False(съедобность), name - индивидуальное название каждого растения
    """

    def __init__(self):
        self.edible = True
        self.name = None


class Mammal(Animal):
    """
    Млекопитающий.
    """

    def __init__(self, name):
        super().__init__()
        self.name = name


class Predator(Animal):
    """
    Хищник.
    """

    def __init__(self, name):
        super().__init__()
        self.name = name


class Fruit(Plant):
    """
    Фрукт.
    """

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.edible = True


class Flower(Plant):
    """
    Цветок.
    """

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.edible = False


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)
