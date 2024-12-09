# Условная конструкция. Операторы if, elif, else
# вариант 4

first = int(input("Задайте first: "))
second = int(input("Задайте second: "))
third = int(input("Задайте third: "))

result = 3 if first == second and second == third else 2 if first == second or second == third or first == third else 0

print(result)
