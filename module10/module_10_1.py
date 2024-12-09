# Домашнее задание по теме "Создание потоков"
import threading
import time


def convert_pretty(td):
    microseconds = int(td * 1000000) % 1000000
    # seconds = int(td) % 60
    # minutes = ( int(td) // 60 ) % 60
    # hours = int(td) // 3600
    minutes, seconds = divmod(int(td), 60)
    hours, minutes = divmod(minutes, 60)
    result = f"{hours}:{minutes:02}:{seconds:02}.{microseconds:06}"
    return result


def write_words(word_count, file_name):
    i = 0
    with open(file_name, "w", encoding="utf-8") as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


if __name__ == "__main__":
    t_start = time.time()
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")
    print("Работа функций " + convert_pretty(time.time() - t_start))

    t_start = time.time()
    threads = [threading.Thread(target=write_words, args=(10, "example5.txt")),
               threading.Thread(target=write_words, args=(30, "example6.txt")),
               threading.Thread(target=write_words, args=(200, "example7.txt")),
               threading.Thread(target=write_words, args=(100, "example8.txt"))]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    print("Работа потоков " + convert_pretty(time.time() - t_start))
