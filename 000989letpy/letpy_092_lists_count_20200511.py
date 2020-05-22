# string = input()
string = 'раз два  три'
string1 = string.split(' ')
print(string1)
countW = 0
for i in range(len(string1)): # стандартная ошибка!!! элементароное незнание синтаксиса.
    if string1[i] == '':
        continue
    countW += 1
    i += 1
print(countW)
