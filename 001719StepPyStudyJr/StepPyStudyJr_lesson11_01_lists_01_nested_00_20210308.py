numbers = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
print(numbers[0])  # numbers[0] = [1, 2, 3]
print(numbers[0][0])  # numbers[0][0] = 1
print(numbers[1][1])  # numbers[1][1] = 20

spells = [['freball', 10, 0], ['metabolism', 0, 8], ['silence', 0, 0]]
for row in spells:
    for elem in row:
        print(elem, ' ',end='')
    print()