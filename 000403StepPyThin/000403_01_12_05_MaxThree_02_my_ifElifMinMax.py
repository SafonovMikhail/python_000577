a = int(input())
b = int(input())
c = int(input())
maxNum = max(a, b, c)
minNum = min(a, b, c)
print(maxNum)
print(minNum)
if ((a > minNum) and (a < maxNum)):
    print(a)
elif ((b > minNum) and (b < maxNum)):
    print(b)
else:
    print(c)
