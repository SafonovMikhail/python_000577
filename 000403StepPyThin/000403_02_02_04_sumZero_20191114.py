a = int(input())
sumBeforeZero = 0
while a != 0:
    sumBeforeZero = sumBeforeZero + a
    a = int(input())
    if a == 0:
        break
print(sumBeforeZero)
