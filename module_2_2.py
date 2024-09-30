# Условная конструкция. Операторы if, elif, else
# вариант 1

first = int( input( "Задайте first: " ) )
second = int( input( "Задайте second: " ) )
third = int( input( "Задайте third: " ) )

result = 0
if ( first == second and second == third ):
    result = 3
elif ( first == second or second == third or first == third ):
    result = 2
print( result )
