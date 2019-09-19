print("000560_03_04_ReturningFromFunction")

print("000560_03_04_ex01_functions_return")
def max(x,y):
	if x>=y:
		return x
	else:
		return y
print ()
print ('max(4,7)')
print (max(4,7))
z=max(8,5)
print ('max(8,5)')
print (z)

print()
print("000560_03_04_task01_functions_return")
def short(x, y):
    if len(x) < len(y):
        return x
    else:
        return y
print('short(\'hello\',\'hi\')')
print(short('hello', 'hi'))

print()
print("000560_03_04_ex02_functions_return")
# код после функции return не выполняется
def short(x,y):
	if len(x)>len(y):
		print ('до \'return\'')
		return x
		print ('после return')
	else:
		print ('до return')
		return y
		print ('после return')
print ('short(\'hello\',\'hi\')')
print (short('hello','hi'))


def add_number(x,y):
	total = x+y
	return total
	print ('this won\'t be printed')
print ('add_number(4,5)')
print (add_number(4,5))

print()
print("000560_03_04_task02_functions_max")
# максимальноео число
def print_nums():
    print(1)
    print(2)
    return
    # после return код не выполняется!
    print(7)
    print(8)
# т.к. не в блоке фукнции, выводится на печать!
# причем, до вывода функции
print(8)
print(9)
print_nums()
