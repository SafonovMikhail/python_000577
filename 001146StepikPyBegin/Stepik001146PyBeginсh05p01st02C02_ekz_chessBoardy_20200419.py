square1 = [int(input()), int(input())]
square2 = [int(input()), int(input())]
if ((square1[0] + square1[1]) % 2 == 0 and (square2[0] + square2[1]) % 2 == 0) or (
        (square1[0] + square1[1]) % 2 != 0 and (square2[0] + square2[1]) % 2 != 0):
    print("YES")
else:
    print("NO")
