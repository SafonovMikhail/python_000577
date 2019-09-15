# 000560_03_04_ex02_functions_return.py
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

input()

def add_number(x,y):
	total = x+y
	return total
	print ('this won\'t be printed')
print ('add_number(4,5)')
print (add_number(4,5))