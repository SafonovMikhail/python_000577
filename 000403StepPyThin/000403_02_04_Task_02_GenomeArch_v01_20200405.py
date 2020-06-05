# s=input()
s1 = 'aaaabbсaa'
x = 0
s2 = ''
for i in s1:  # нетвердое знание синтаксиса range (просто не нужно range)
    if s1[i] == s1[i + 1]:
        x += 1
    s2 = s2.append(i + str(x))
print(i)
'''count = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1

    print(s[i] + str(count), end='')
# print()'''
