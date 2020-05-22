# s=input()
s = 'aaaabbсaa'

s1 = s1.add
count = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1

    print(s[i] + str(count), end='')
# print()
