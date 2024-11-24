# Условная конструкция. Операторы if, elif, else
# вариант 3

first = int( input( "Задайте first: " ) )
second = int( input( "Задайте second: " ) )
third = int( input( "Задайте third: " ) )

result = 0
result += 1 if ( first == second ) else 0
result += 1 if ( second == third ) else 0
result += 1 if ( first == third ) else 0
result = 2 if ( result == 1 ) else result

print( result )
1