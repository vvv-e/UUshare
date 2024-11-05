# Дополнительное практическое задание по модулю: Базовые структуры данных.

# входные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

def stu_avg(students_, grades_):
    return {sorted(students_)[num]: round(sum(grades_[num]) / len(grades_[num]), 1) for num in range(len(grades_))}

print(stu_avg(students, grades))

# не самое оптимальное решение по времени выполнения :-(, но в одну строку!!!
