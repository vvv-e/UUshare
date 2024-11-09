# Домашнее задание по теме "Множественное наследование"
import random


# класс описывающий животных
class Animal:
    live = True
    sound = None  # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве.
        self.speed = speed  # скорость передвижения существа(определяется при создании объекта)

    # должен менять соответствующие координаты в _cords на dx, dy и dz в том же порядке, где множителем
    # будет являться speed. Если при попытке изменения координаты z в _cords значение будет меньше 0, то выводить
    # сообщение "It's too deep, i can't dive :(", при этом изменения не вносятся.
    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    # выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    # выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и
    # "Be careful, i'm attacking you 0_0", если больше.
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    # выводит строку со звуком sound.
    def speak(self):
        print(self.sound)


# класс описывающий птиц. Наследуется от Animal.
class Bird(Animal):
    beak = True  # наличие клюва

    def __init__(self, speed):
        super().__init__(speed)

    # выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")


# класс описывающий плавающего животного. Наследуется от Animal.
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    # где dz изменение координаты z в _cords. Должен изменять в отрицательную сторону координату z уменьшенную в 2 раза с
    # учётом скорости. С каким бы знаком не был передан параметр dz, внутри метода используйте его значение по
    # модулю (функция abs).
    def dive_in(self, dz):
        self._cords[2] -= dz // 2 * abs(self.speed)


# класс описывающий ядовитых животных. Наследуется от Animal.
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)


# класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
# Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"  # звук, который издаёт утконос

    def __init__(self, speed):
        super().__init__(speed)


if __name__ == '__main__':
    db = Duckbill(10)
    print(db.live)
    print(db.beak)
    db.speak()
    db.attack()
    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()
    db.lay_eggs()
