# Дополнительное практическое задание по модулю: "Основные операторы".

def get_password( x = 3 ):
    if x < 3 or x > 20:
        return "Неверное число на первом камне: " + str(x)
    x_str = str(x) + " - "
    old =[]
    for i in range( 1, x ):
        for j in range( 2, x ):
            if i == j:
                continue
            elif x % (i+j) == 0:
                if [i,j] in old or [j,i] in old:
                    continue
                else:
                    x_str += str(i) + str(j)
                    old.append([i,j])
    return ( x_str )

for i in range( 3, 21 ):
   print( "Пароль на втором камне для числа:", get_password( i ))




