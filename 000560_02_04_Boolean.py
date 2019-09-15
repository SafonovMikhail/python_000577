print("")
print("000560_02_04_ex01_bool:AND")
print(1 == 1 and 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(1 < 2 and 3 > 6)

print("000560_02_04_task01_bool:AND")
if (1 == 1) and (2 + 2 > 3):
    print('true')
else:
    print('false')
print("")
print("000560_02_04_ex02_bool:OR")
print(1 == 1 or 2 == 2)
print(1 == 1 or 2 > 3)
print(1 != 1 or 2 == 2)
print(1 > 2 or 3 > 6)

print("000560_02_04_task02_bool:OR")
age = 15
money = 500
if age > 18 or money > 100:
    print('welcome!')

print("")
print("bool:NOT")
print(not 1 == 1)
print(not 1 > 7)
print("000560_02_04_ex03_bool:NOT")
print(not 2 == 2)
print(1 == 1 and 2 == 3)
print(1 != 1 and 2 == 2)
print(1 < 2 and 3 > 6)
print("000560_02_04_task03_bool:NOT")
if not True:
	print('1')
elif not (1+1==3):
	print ('2')#выводится на печать
else:
	print ('3')
