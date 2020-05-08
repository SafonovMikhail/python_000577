p1 = [int(input()), int(input())]
p2 = [int(input()), int(input())]
print(p1, p2)
p3 = p1 + p2
print(max(p3))
if (p1[0] == p2[0] or p1[1] == p2[1]) and max(p3) <= 8:
    print("YES")
else:
    print("NO")
