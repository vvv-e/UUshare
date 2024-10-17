# Дополнительное практическое задание по модулю: "Основные операторы".
# Вариант 2, оптимизированный.

import time

def get_password(x=3):
    #    if x < 3 or x > 20:
    #        return "Неверное число на первом камне: " + str(x)
    start_time = time.time()
    x_str = str(x) + " - "
    for i in range(1, x // 2 + 1):
        for j in range(i + 1, x - i + 1):
            if x % (i + j) == 0:
                x_str += str(i) + str(j)
    print("время выполнения", time.time() - start_time)
    return (x_str)

# for i in range( 3, 21 ):
#   print( "Пароль на втором камне для числа:", get_password( i ))

print("Пароль на втором камне для числа:", get_password(10000))
print("Пароль на втором камне для числа:", get_password(20))
