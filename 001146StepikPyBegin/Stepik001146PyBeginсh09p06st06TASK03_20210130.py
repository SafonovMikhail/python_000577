# indent = int(input())
# indent = 1
# indent = 14
# str1 = input()
# str1 = 'bwfusvfupdbftbs'
# str1 = 'fsfftsfufksttskskt'
'''
str1 = '0123456789'
for i in str1:
    print(chr((ord(i) + indent) % 26), end='')
'''
indent = 14
# str1 = '0123456789'
str1 = 'abcdefghijklmnopqrstuvwxyz'
str2 = ''
str3 = ''
str5_coded = 'fsfftsfufksttskskt'
for i in range(len(str1)):
    if i < indent:
        str3 += str1[i]
        # print('str3:', str3)
    if (i + indent) < len(str1):
        str2 += str1[i + indent]
        # print('str2:', str2)
str4 = str2 + str3
print()
print('str1:', str1)
# print('str3:', str3)
# print('str2:', str2)
print('str4:', str4)
print('str5_coded:', str5_coded)
for i in str5_coded:
    for j in str4:
        if i == j:
            print(str1[str4.find(j)], end='')

print('final solution')

indent = int(input())
str1 = 'abcdefghijklmnopqrstuvwxyz'
str2 = ''
str3 = ''
str5_coded = input()
for i in range(len(str1)):
    if i < indent:
        str3 += str1[i]
    if (i + indent) < len(str1):
        str2 += str1[i + indent]
str4 = str2 + str3
for i in str5_coded:
    for j in str4:
        if i == j:
            print(str1[str4.find(j)], end='')

'''
Шифр Цезаря 🌶️
Легион Цезаря, созданный в 23 веке на основе Римской Империи не изменяет
древним традициям и использует шифр Цезаря. Это их и подвело, ведь данный шифр
очень простой. Однако в постапокалипсисе люди плохо знают все тонкости довоенного мира,
поэтому ученые из НКР не могут понять как именно нужно декодировать данные сообщения.
Напишите программу для декодирования этого шифра.

Формат входных данных
В первой строке дается число n (1≤ n≤ 25) – сдвиг,
во второй строке даётся закодированное сообщение в виде строки со строчными
латинскими буквами.

Формат выходных данных
Программа должна вывести одну строку – декодированное сообщение. Обратите внимание,
что нужно декодировать сообщение, а не закодировать.

Sample Input 1:

1
bwfusvfupdbftbs
Sample Output 1:

avetruetocaesar
Sample Input 2:

14
fsfftsfufksttskskt
Sample Output 2:

rerrfergrweffewewf

'''
