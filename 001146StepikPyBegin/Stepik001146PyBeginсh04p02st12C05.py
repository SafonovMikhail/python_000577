a, b, c = int(input()), int(input()), int(input())
# a, b, c = 3, 2, 1
list = [a, b, c]
print(list)
list2 = sorted(list)
if list2[3] < list2[2] + list2[1]:
    print("YES")
else:
    print("NO")
