lyear = int(input())
if (lyear % 4 == 0 and lyear % 100 != 0) or lyear % 400 == 0:
    print("YES")
else:
    print("NO")
