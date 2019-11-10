a = int(input())
b = int(input())
c = int(input())
if a - b < 0:
    a, b = b, a
if a - c < 0:
    a, c = c, a
if b - c < 0:
    b, c = c, b
print(a)
print(c)
print(b)
# maxNum = max(a, b, c)
# minNum = min(a, b, c)
# print(maxNum)
# print(minNum)
# if ((a > minNum) and (a < maxNum)):
#     print(a)
# elif ((b > minNum) and (b < maxNum)):
#     print(b)
# else:
#     print(c)
