# Дополнительное практическое задание по модулю: "Подробнее о функциях."

# исходные данные
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

# функция суммирует "все подряд"
def calculate_structure_sum( ds ):
    if type(ds) == str:
        return len(ds)
    elif type(ds) == int or type(ds) == float:
        return ds
    elif type(ds) == list or type(ds) == tuple or type(ds) == set:
        sum = 0
        for i in ds:
            sum += calculate_structure_sum(i)
        return sum
    elif type(ds) == dict:
        sum = 0
        for key, i in ds.items():
            sum += calculate_structure_sum(key) + calculate_structure_sum(i)
        return sum
    else:
        print("что-то пошло не так, неожиданный тип:", type(ds))
        return(0)


result = calculate_structure_sum(data_structure)
print(result)
