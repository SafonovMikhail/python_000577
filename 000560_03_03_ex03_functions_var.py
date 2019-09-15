# 000560_03_03_ex03_functions_var.py
# аргументы принимает переменную
# нельзя ссылаться извне

def func(variable):
	variable +=1
	print (variable)
func(7)
print (variable)

input()