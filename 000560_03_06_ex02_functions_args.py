# 000560_03_06_ex02_functions_args.py
# переменной можно назначить функцию

def add(x,y):
	return x + y

def do_twice(func, x,y):
	return func(func(x,y), func(x,y))

a=5
b=10

print (do_twice(add, a,b))