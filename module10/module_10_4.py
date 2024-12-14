# Домашнее задание по теме "Очереди для обмена данными между потоками."
import threading
from itertools import filterfalse
from random import randint
from threading import Thread
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.tables = [tbl for tbl in args]
        self.queue = Queue()

    # прибытие гостей
    def guest_arrival(self, *guests):
        for guest in guests:  # для всех гостей
            evrika = False
            for tbl in self.tables:  # проверить есть ли свободный стол
                if tbl.guest is None:  # посадить гостя за стол
                    tbl.guest = guest
                    print(f"{guest.name} сел(-а) за стол номер {tbl.number}\n", end="")
                    guest.start()
                    evrika = True
                    break
            if not evrika:
                print(f"{guest.name} в очереди\n", end="")
                self.queue.put(guest)

    # проверяет все ли столы пусты
    def empty_tables(self):
        evrika_not_empty = False
        for tbl in self.tables:  # проверить есть ли не свободный стол
            if not tbl.guest is None:
                evrika_not_empty = True
                break
        return not evrika_not_empty

    # обслужить гостей
    def discuss_guests(self):
        while not self.queue.empty() or not self.empty_tables():
            for tbl in self.tables:
                if not tbl.guest is None and not tbl.guest.is_alive():  # если гость покушал
                    print(f"{tbl.guest.name} покушал(-а) и ушёл(ушла)\n", end="")
                    print(f"Стол номер {tbl.number} свободен\n", end="")
                    tbl.guest = None
                if tbl.guest is None and not self.queue.empty():  # посадить гостя за стол
                    tbl.guest = self.queue.get()
                    print(f"{tbl.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {tbl.number}\n",
                          end="")
                    tbl.guest.start()


if __name__ == "__main__":
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
