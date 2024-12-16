# Домашнее задание по теме "Многопроцессное программирование"
import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        while True:
            line = file.readline()
            if not line:  # если конец файла
                break
            else:  # иначе не конец файла
                all_data.append(line)
        # print(len(all_data))


if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов 1
    start = datetime.datetime.now()
    for fn in filenames:
        read_info(fn)
    stop = datetime.datetime.now()
    print(stop - start, "(линейный 1)")

    # Многопроцессный
    start = datetime.datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    stop = datetime.datetime.now()
    print(stop - start, "(многопроцессный)")

    # Линейный вызов 2
    start = datetime.datetime.now()
    for fn in filenames:
        read_info(fn)
    stop = datetime.datetime.now()
    print(stop - start, "(линейный 2)")
