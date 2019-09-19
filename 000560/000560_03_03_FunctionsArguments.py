# 000560_03_03_FunctionsArguments.py

print()
print("000560_03_03_ex01_functions_arg")
# функции принимают аргументы
def print_with_exclamation(word):
	print (word + '!')
print_with_exclamation('spam')
print_with_exclamation('eggs')
print_with_exclamation('python')

print()
print("000560_03_03_task01_functions_double")
# функции принимают аргументы
def print_double(x):
    print(2 * x)
print_double(3)

print()
print("000560_03_03_ex02_functions_twoArgs")
# аргументы через запятую
def print_sum_twice(x,y):
	print (x+y)
	# print (x+y)
print_sum_twice(3,10)

print()
print("000560_03_03_task02_functions_twoArgs_mult")
# аргументы через запятую
def print_mult(x, y):
    print(x * y)
# print (x*y)
print_mult(3, 10)

print()
print("000560_03_03_ex03_functions_var")
# аргументы принимает переменную
# нельзя ссылаться извне
def func(variable):
	variable +=1
	print (variable)
func(7)
# print (variable)
#  раскомментить, будет ошибка

print()
print("000560_03_03_task03_functions_IF")
def even(x):
    if x % 2 == 0:
        print('y')
    else:
        print('n')
even(3)
