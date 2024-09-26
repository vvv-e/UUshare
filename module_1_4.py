# Организация программ и методы строк

my_string = input( "произвольный текст: " )      # ввод строки с консоли

print( "количество символов в строке=", len(my_string))
print( my_string.upper() )                       # строка в верхнем регистре
print( my_string.lower() )                       # строка в нижнем регистре
print( my_string.replace( " ", "") ) # удалить все пробелы
print( my_string[0] )                            # первый символ строки
print( my_string[-1] )                           # последний символ строки