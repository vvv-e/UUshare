# Домашняя работа по уроку "Модули и пакеты"

from modul1.fake_math import divide as fake_divide
from modul1.true_math import divide as true_divide

if __name__ == '__main__':
    result1 = fake_divide(69, 3)
    result2 = fake_divide(3, 0)
    result3 = true_divide(49, 7)
    result4 = true_divide(15, 0)
    print(result1)
    print(result2)
    print(result3)
    print(result4)


