# Самостоятельная работа по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, 'two', True]
print_params(*values_list)

values_dict = {'a': 1, 'b': 'two', 'c': True}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
