# Функции в Python.Функция с параметром.

def get_matrix( n = 0, m = 0, value = 0 ):
    matrix = []
    if n < 0 or m < 0:
        return matrix
    for i in range( 0, n ):
        matrix.append( [] )
        for j in range( 0, m ):
            matrix[i].append( value )
    return matrix

print( get_matrix(2,2,10) )
print( get_matrix(3,5,42) )
print( get_matrix(4,2,13) )
print( get_matrix() )
print( get_matrix(5,-2,10) )


