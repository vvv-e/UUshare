# Дополнительное практическое задание по модулю: Базовые структуры данных.

# входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

def stu_avg(students, grades):
    return {sorted(students)[num]: round(sum(grades[num]) / len(grades[num]), 1) for num in range(len(grades))}

print(stu_avg(students, grades))

# не самое оптимальное решение по времени выполнения :-(