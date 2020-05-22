str = 'abrakadabra'
sum = 0
# print(type(sum[1]))
for i in range(len(str)):
    print(str[i])
for i in str:
    print(i, sep="@", end='_')
#     sep="@" не работает, т.к. выводится по одному индексу.
#     if str[i] == 'a':
#         sum += 1
# print(sum)
