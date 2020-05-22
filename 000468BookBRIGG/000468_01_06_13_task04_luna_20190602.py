from typing import Any

weight = float(input('Введите Ваш вес: '))  # type: Any
age = int(input('Введите Ваш возраст(полных лет): '))
weightLuna=weight*0.165
for i in range(age+1,age+1+15):
	weightLuna=weightLuna+0.165
	print ('вам '+ str(i)+'  Ваш вес на Луне '+ str(weightLuna))
input()