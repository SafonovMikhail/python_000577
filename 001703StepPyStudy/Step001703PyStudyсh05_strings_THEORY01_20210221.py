# ----------------------------
print('# 1. Строки')
# s = input()
s = 'love'
print(len(s))
# t = input()
t = '5'
number = int(t)
u = str(number)
print(s * 3)
print(s + ' ' + u)
print()

# ----------------------------
print('# 2. Срезы (slices)')
s = 'abcdefg'
print(s)
print('s[1]', s[1])
print('s[-1]', s[-1])
print('s[1:3]', s[1:3])
print('s[1:-1]', s[1:-1])
print('s[:3]', s[:3])
print('s[2:]', s[2:])
print('s[:-1]', s[:-1])
print('s[::2]', s[::2])
print('s[1::2]', s[1::2])
print('s[::-1]', s[::-1])
print()

# ----------------------------
print('# 3. Методы')
S = 'Hello'
print(S.find('e'))  # вернёт 1
print(S.find('ll'))  # вернёт 2
print(S.find('L'))  # вернёт -1
print()
S = 'Hello'
print(S.find('l'))
# вернёт 2
print(S.rfind('l'))
# вернёт 3

print('Hello'.replace('l', 'L'))
# вернёт 'HeLLo'

print('Abrakadabra'.replace('a', 'A', 2)) # вернёт 'AbrAkAdabra'