# string = input()
string = 'Восклицательного'

i = 0
while i < len(string):
    if string[i] == '!':
        break
    print(string[i])
    i = i + 1
else:
    print('Восклицательного знака не найдено')