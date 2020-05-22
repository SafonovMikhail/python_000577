i = 0
while i < 5:
    print("01:", i)
    i += 1

print()

for i in range(5):  # один аргумент
    print("02:", i)

print()

for i in range(5, 8):  # два аргумента
    print("two args(5, 8):", i)

print()

for i in range(1, 10, 3):  # три аргумента
    print("three args(1, 10, 3):", i)

print()

for i in range(10, 1, -3):  # три аргумента
    print("three args(10, 1, -3):", i)
