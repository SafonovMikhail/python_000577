'''
Дано натуральное число (n≤9). Напишите программу,
которая печатает таблицу размером n×5,
где в i-ой строке указано число i (числа отделены одним пробелом).
'''
num = int(input())
# num = 8
for i in range(1, num + 1):
    j = 1
    while j < 6:
        print(f'{i} ', end='')
        j += 1
    print()
