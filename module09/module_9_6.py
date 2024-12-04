# Домашнее задание по теме "Генераторы"

def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j:j + i + 1]


if __name__ == "__main__":
    a = all_variants("abc")
    for s in a:
        print(s)
