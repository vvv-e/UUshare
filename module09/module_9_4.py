# Домашнее задание по теме "Создание функций на лету"
from random import choice

if __name__ == "__main__":
    # Lambda-функция:
    first = 'Мама мыла раму'
    second = 'Рамена мало было'
    res = list(map(lambda x, y: x == y, first, second))
    print(res)


    # Замыкание:
    def get_advanced_writer(file_name):
        def write_everything(*data_set):
            with open(file_name, "a", encoding="utf-8") as file:
                for ds in data_set:
                    file.write(str(ds) + "\n")

        return write_everything


    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


    # Метод __call__:
    class MysticBall:
        def __init__(self, *args):
            self.words = args

        def __call__(self):
            return choice(self.words)


    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())
