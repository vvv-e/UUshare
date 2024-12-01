# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y)]
second_result = [not bool(len(first[i]) - len(second[i])) for i in range(min(len(first), len(second)))]

if __name__ == "__main__":
    print(list(first_result))
    print(list(second_result))
