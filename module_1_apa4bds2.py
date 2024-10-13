# Дополнительное практическое задание по модулю: Базовые структуры данных.

# входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

stu_avg = {}
students = sorted( list( students ) )
for i in range(len(students)):
    stu_avg[students[i]] = float(sum(grades[i])) / float(len(grades[i]))
print( stu_avg )

