# Домашнее задание по теме "Блокировки и обработка ошибок"
import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0  # баланс банка(int)
        self.lock = threading.Lock()  # объект класса Lock для блокировки потоков.
        self.run_deposit = False  # флаг работы депозита, для исключения блокировок

    def deposit(self):
        self.run_deposit = True
        for i_trans in range(100):
            money_cash = randint(50, 500)  # положить на депозит
            self.balance += money_cash
            sleep(0.001)
            print(f"Пополнение: {money_cash}. Баланс: {self.balance}\n", end="")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
        self.run_deposit = False
        if self.lock.locked():  # разблокировать замок при окончании deposit
            self.lock.release()

    def take(self):
        for i_trans in range(100):
            non_cash_money = randint(50, 500)  # снять с депозита
            print(f"Запрос на {non_cash_money}\n", end="")
            if self.balance >= non_cash_money:
                self.balance -= non_cash_money
                sleep(0.001)
                print(f"Снятие: {non_cash_money}. Баланс: {self.balance}\n", end="")
            else:
                print("Запрос отклонён, недостаточно средств\n", end="")
                if self.run_deposit:  # устанавливать блокировки только при работающем deposit
                    if not self.lock.locked():  # 1-я строка. Конструкция из 3-х строк, для блокирования потока take
                        self.lock.acquire()  # 2-ая строка
                    self.lock.acquire()  # 3-я строка
                else:  # если deposit не работает, то закончить работу без блокировок
                    continue


if __name__ == "__main__":
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
