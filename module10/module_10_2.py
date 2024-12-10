# Домашнее задание по теме "Потоки на классах"
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!\n", end="")
        enemy = 100  # количество врагов
        days = 0  # сражается дней
        while enemy > 0:
            days += 1
            enemy -= self.power
            print(f"{self.name} сражается {days} дней(дня)..., осталось {enemy} воинов.\n", end="")
            sleep(1)
        print(f"{self.name} одержал победу спустя {days} дней(дня)!\n", end="")


if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print("Все битвы закончились!")
