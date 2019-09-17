#000560_02_12_ex01_SimpleCalc_WhileQuit.py
# рассмотрим главное меню

# while  True:
# 	print ('Options')
# 	print ('Enter "add" to add two numbers')
# 	print ('Enter "subs" to substract two numbers')
# 	print ('Enter "mult" to multiply two numbers')
# 	print ('Enter "div" to divide two numbers')
# 	print ('Enter "end" to end the programm')
# 	user_input = ('>>> ') # я не вижу, как мне дается возможность ввести с клавиатуры?
#
# 	if user_input == 'quit':
# 		break
# 	elif user_input == 'add':
# 		...
# 	elif user_input == 'subs':
# 		...
# 	elif user_input == 'mult':
# 		...
# 	elif user_input == 'div':
# 		...
# 	else:
# 		print ('unknown input')

# 000560_02_12_ex02_SimpleCalc_elif.py
# рассмотрим главное меню
while True:
	print('\nOptions')
	print('Enter "add" to add two numbers')
	print('Enter "subs" to substract two numbers')
	print('Enter "mult" to multiply two numbers')
	print('Enter "div" to divide two numbers')
	print('Enter "end" to end the programm')
	print('Enter "q" to end the programm')
	user_input = input('>>> ')  # я не вижу, как мне дается возможность ввести с клавиатуры?

	if user_input == 'q':
		break
		# continue
	else:
		num1 = float(input('Enter 1st num: '))
		num2 = float(input('Enter 2nd num: '))
		if user_input == 'add':  # допустил ошибку! Присваивание(=) вместо равно (==)
			result = str(num1 + num2)
			print('The answer is', result)
		elif user_input == 'subs':
			result = str(num1 - num2)
			print('The answer is', result)
		elif user_input == 'mult':
			result = str(num1 * num2)
			print('The answer is', result)
		elif user_input == 'div':
			result = str(num1 / num2)
			print('The answer is', result)
		else:
			print('unknown input')


#000560_02_12_task03_SimpleCalc_mult.py

# elif user_input == 'multiply':
# 	num1 = float ('Enter a number: ')
# 	num2 = float ('Enter a number: ')
# 	result = str(num1 * num2)
# 	print ('the answer is ', result)