#  Домашнее задание по теме "Оператор "with"
import re

class WordsFinder:

    # в задании указан конструктор WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
    # надеюсь, что случайно не указаны апострофы в конце первого и вначале второго параметра, которые там есть
    def __init__(self, *args):
        self.file_names = []
        for fn in args:
            self.file_names.append(fn)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for fn in self.file_names:
            with open(fn, encoding="utf-8") as file:
                print(file.read().lower())

        pass

    def find(self, word):
        pass

    def count(self, word):
        pass

if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего


