square1 = [int(input()), int(input())]
square2 = [int(input()), int(input())]

if min(square1 + square2) < 1 or max(square1 + square2) > 8:
    print("NO1")
elif abs(square1[0] - square2[0]) > 8 or abs(square1[1] - square2[1]) > 8:
    print("NO2")
elif abs(square1[0] - square2[0]) == abs(square1[1] - square2[1]):
    print("YES")
else:
    print("NO3")
