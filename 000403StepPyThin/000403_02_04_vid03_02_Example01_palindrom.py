# pal = input()
# pal = '123321'
# import string
import time

pal = 'c1ggtgg2c'
start = time.time()
# pal = 'А роза упала на лапу Азора'
pal = pal.upper().replace(" ", "")
print(pal)
count = 0
for i in range(len(pal)):
    if pal[i - 1] == pal[-i]:
        count += 1
if len(pal) == count:
    print("pal")
print('----- %s ----- sec ' % (time.time() - start))
print(count)
print(len(pal))

print()

# s = input()
s = pal
print(s)
i = 0  # счетчик 1
j = len(s) - 1  # счетчик 2
is_pal = True
while i < j:
    if s[i] != s[j]:
        is_pal = False
        break
    i += 1
    j -= 1
if is_pal:
    print('Y')
else:
    print('N')

pal = 'c2ggtgg2c'
s = pal
print(s)
i = 0  # счетчик 1
j = len(s) - 1  # счетчик 2
is_pal = True
while i < j:
    if s[i] != s[j]:
        is_pal = False
        break
    i += 1
    j -= 1
if is_pal:
    print('Y')
else:
    print('N')
