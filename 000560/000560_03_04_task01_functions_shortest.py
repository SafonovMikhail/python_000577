# 000560_03_04_ex01_functions_return.py

def short(x,y):
	if len(x)>len(y):
		return x
	else:
		return y

print ('short(\'hello\',\'hi\')')
print (short('hello','hi'))

input()