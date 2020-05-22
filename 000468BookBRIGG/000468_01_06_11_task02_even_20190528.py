age = int(input('Введите Ваш возраст: '))
if age%2==0:
	for i in range(0,age):
		if i%2==0:
			print (i+2)
elif age%2 !=0:
	for i in range(0,age+1):
		if i%2 !=0:
			print (i)
input() 