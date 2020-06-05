# s1 = 'aaaabbсaa'
s1 = 'abс'
count = 1
for i in range(len(s1) - 1):
    if s1[i] == s1[i + 1]:
        count += 1
        continue
    print(s1[i] + str(count), end='')
    count = 1
print(s1[i] + str(count), end='')
