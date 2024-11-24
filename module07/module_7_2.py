# Домашнее задание по теме "Позиционирование в файле"

def custom_write(file_name, strings):
    file = open(file_name, "w", encoding="utf-8")
    res_dict = {}
    for st in strings:
        res_dict[(len(res_dict) + 1, file.tell())] = st
        file.write(f"{st}\n")
    file.close()
    return res_dict


if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
