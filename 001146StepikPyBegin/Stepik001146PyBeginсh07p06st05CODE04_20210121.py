'''
что покажет приведенный фрагмент кода
'''

result = 0
for i in range(10):
    if i % 2 == 0:
        continue
    result += i
print(result)