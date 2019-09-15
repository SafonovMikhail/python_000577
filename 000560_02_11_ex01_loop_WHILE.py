#000560_02_11_ex01_loop_WHILE.py
# 
print()
words = ['hello','words','spam','eggs']
counter = 0 # объявляем переменную-счетчик
max_index = len(words) - 1 # максимальный индекс в списке

while counter <= max_index:
	word = words[counter] # перебор всех слов
	print (word, '!')
	counter = counter + 1
