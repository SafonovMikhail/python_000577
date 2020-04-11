allnums = [1, 2, 3, 4, 5]
for i in range(len(allnums)):
    print(i)
print('')
for i in range(len(allnums)):
    if i % 2 == 0:
        print(i)
print('')
for i in range(len(allnums)):
    if i == 0 or i == 3 or i == 4:
        print(i)
print('')
new_nums = []
print('for i in range(len(allnums)): ')
for i in range(len(allnums)):
    if i == 0 or i == 3 or i == 4:
        new_nums.append(allnums[i])
print(new_nums)
# 2020-02-26