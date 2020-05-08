p1 = [int(input()), int(input())]
p2 = [int(input()), int(input())]
# print(p1, p2)
p3 = p1 + p2
# print(max(p3))
if (abs(p1[0] - p2[0]) <= 1 and abs(p1[1] - p2[1]) <= 1) and (
        abs(p1[0] + p2[0]) < 16 and abs(p1[1] + p2[1]) < 16) and max(p3) <= 8:
    print("YES")
else:
    print("NO")