month = int(input())
list1 = [1, 3, 5, 7, 8, 10, 12]
if month in list1:
    print(31)
elif month == 2:
    print(28)
else:
    print(30)
