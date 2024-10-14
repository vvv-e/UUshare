# Дополнительное практическое задание по модулю: Базовые структуры данных.

# входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

stu_avg = {}               # создать пустой соварь
students = sorted( list( students ) ) # преобразовать в лист и сортировать
i = 0                                 # индекс студента
for item_s in students:
    average = 0.                      # средняя оценка
    for items_d in grades[i]:
        average += float(items_d)
    average /= float(len(grades[i]))
    i += 1
    stu_avg[item_s] = average         # добавить в словарь студента и среднюю оценку
print( stu_avg )           # вывод результата в консоль

