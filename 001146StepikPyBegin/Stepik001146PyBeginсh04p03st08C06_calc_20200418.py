list1 = int(input()), int(input()), (input())
if list1[2] == "*":
    print(list1[0] * list1[1])
elif list1[2] == "+":
    print(list1[0] + list1[1])
elif list1[2] == "/":
    if list1[1] == 0:
        print("На ноль делить нельзя!")
    else:
        print(list1[0] / list1[1])
elif list1[2] == "-":
    print(list1[0] - list1[1])
else:
    print("Неверная операция")