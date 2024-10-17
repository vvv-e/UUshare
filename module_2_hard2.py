# Дополнительное практическое задание по модулю: "Основные операторы".
# Вариант 2, оптимизированный.

def get_password( x = 3 ):
    if x < 3 or x > 20:
        return "Неверное число на первом камне: " + str(x)
    x_str = str(x) + " - "
    for i in range( 1, x ):
        for j in range( i+1, x ):
            if x % (i+j) == 0:
                x_str += str(i) + str(j)
    return ( x_str )

for i in range( 3, 21 ):
   print( "Пароль на втором камне для числа:", get_password( i ))




