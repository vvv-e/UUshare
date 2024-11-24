# Условная конструкция. Операторы if, elif, else
# вариант 2

first = int( input( "Задайте first: " ) )
second = int( input( "Задайте second: " ) )
third = int( input( "Задайте third: " ) )

result = 0
if ( first == second ):
    result += 1
if ( second == third ):
    result += 1
if ( first == third ):
    result += 1
if ( result == 1 ):
    result = 2

print( result )
