'''
Напишите программу подсчета букв ‘a’ в строке «abrakadabra»
Selfedu001133PyBeginCh03p02TASK01
'''

str = 'abrakadabra'
count = 0
for i in range(len(str)):
    if str[i] == 'a':
        count += 1
print(count)
