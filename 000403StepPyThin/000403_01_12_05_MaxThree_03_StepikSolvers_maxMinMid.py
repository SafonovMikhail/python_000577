a, b, c = int(input()), int(input()), int(input())
maxNum = max(a, b, c)
minNum = min(a, b, c)
mid = (a + b + c) - maxNum - minNum
print(maxNum, "\n", minNum, "\n", mid)
