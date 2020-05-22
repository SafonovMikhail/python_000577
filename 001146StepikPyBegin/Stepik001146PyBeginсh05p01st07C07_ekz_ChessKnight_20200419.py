square1 = [int(input()), int(input())]
square2 = [int(input()), int(input())]

# square1 = [3, 3]
# square2 = [5, 4]
# square2 = [2, 1]
# square2 = [1, 3]
# square2 = [6, 4]
# square2 = [2, 1]
# square2 = [2, 1]
# square2 = [2, 1]


if min(square1 + square2) < 1 or max(square1 + square2) > 8:
    print("NO")
elif abs(square1[0] - square2[0]) == abs(square1[1] - square2[1]):
    print("NO")
elif abs(square1[0] - square2[0]) > 2 or abs(square1[1] - square2[1]) > 2:
    print("NO")
elif square1[0] == square2[0] or square1[1] == square2[1]:
    print("NO")
else:
    print("YES")
