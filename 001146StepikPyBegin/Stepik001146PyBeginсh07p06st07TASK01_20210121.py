num = int(input())
# num = 4
for i in range(2, num + 1):
    if num % i == 0:
        print(i)
        break
if num == 1:
    print(f'{num}')
'''
На вход программе подается число n>1.
Напишите программу, которая выводит его наименьший отличный от 1 делитель.
'''
