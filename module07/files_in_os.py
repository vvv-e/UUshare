# Домашнее задание по теме "Файлы в операционной системе"
import os, time

if __name__ == "__main__":
    directory = "."
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.stat(file).st_mtime
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.stat(file).st_size
            parent_dir = os.path.dirname(filepath)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
                  f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
