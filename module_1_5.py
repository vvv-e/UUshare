# Неизменяемые и изменяемые объекты. Кортежи и списки

immutable_var = ( 1, 1., [1], (1, 1., [1]) )
print( "Immutable tuple:", immutable_var )
# immutable_var[0] = 2 TypeError: 'tuple' object does not support item assignment

mutable_list = [1, 1., (1,1), [1, 1., (1,1)]]
print( "Mutable list:", mutable_list )
mutable_list[2] = (2,2)
print( "Mutable list edt:", mutable_list )
