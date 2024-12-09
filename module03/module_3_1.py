# Домашняя работа по уроку "Пространство имён".

calls = 0

# подсчитывает вызовы функций
def count_calls():
    global calls
    calls += 1

# принимает аргумент - строку
# возвращает кортеж из: длины строки, строку в верхнем регистре, строку в нижнем регистре
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

# принимает два аргумента: строку и список,
# возвращает True, если строка находится в этом списке, False - если отсутствует
# регистром строки при проверке пренебрегает
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.upper() == i.upper():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

