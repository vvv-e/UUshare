# Условная конструкция. Операторы if, elif, else
# вариант 1

first = int( input( "Задайте first: " ) )
second = int( input( "Задайте second: " ) )
third = int( input( "Задайте third: " ) )

if ( first == second and second == third ):
    result = 3
elif ( first == second or second == third or first == third ):
    result = 2
else:
    result = 0

print( result )
