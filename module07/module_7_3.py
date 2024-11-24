#  Домашнее задание по теме "Оператор "with"
import re

class WordsFinder:

    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        for fn in self.file_names:
            try:
                with open(fn, encoding="utf-8") as file:
                    lst = []
                    # punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for wrd in re.split(r'[,.=\n!?;: ]+', file.read().lower()):
                        if wrd != "" and wrd != "-":
                            lst.append(wrd)
                    all_words[fn] = lst
            except FileNotFoundError:
                all_words[fn] = []
        return all_words

    def find(self, word):
        dct = {}
        for name, words in self.get_all_words().items():
            try:
                i = words.index(word.lower()) + 1
            except ValueError:
                i = None
            dct[name] = i
        return dct
        # return {name: words.index(word.lower()) + 1 for name, words in self.get_all_words().items()}


    def count(self, word):
        return {name: words.count(word.lower()) for name, words in self.get_all_words().items()}


if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    print("-" * 60)

    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                          'Rudyard Kipling - If.txt',
                          'Mother Goose - Monday’s Child.txt')
    print(finder1.get_all_words())
    print(finder1.find('the'))
    print(finder1.count('the'))
