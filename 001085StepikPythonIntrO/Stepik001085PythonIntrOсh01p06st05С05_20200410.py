x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (1 <= (x1 and x2 and y1 and y2) <= 8) and (x1 != x2 and y1 != y2):
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
