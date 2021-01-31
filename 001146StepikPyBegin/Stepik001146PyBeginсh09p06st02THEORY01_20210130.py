print('Функция ord:')

num1 = ord('A')
num2 = ord('B')
num3 = ord('a')
print(num1, num2, num3)

print('Функция chr:')

chr1 = chr(65)
chr2 = chr(75)
chr3 = chr(110)
print(chr1, chr2, chr3)

print('Вывод загланых букв английского алфавита:')

for i in range(26):
    print(chr(ord('A') + i), end='')

print()
if 'b' > 'a':
    print('Больше')

# add

for i in range(26):
    print(chr(ord('a') + i), end='')
