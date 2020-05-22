amount = int(input())
# amount = 157
sum1 = 0
# 1,5,10,25
# print("25: ", amount // 25)
sum1 += amount // 25
# print("остаток: ", amount % 25)
part1 = amount % 25
# print("10: ", part1 // 10)
sum1 += part1 // 10
# print("остаток: ", part1 % 10)
part1 = part1 % 10
# print("5: ", part1 // 5)
sum1 += part1 // 5
# print("остаток: ", part1 % 5)
part1 = part1 % 5
# print("1: ", part1 // 1)
sum1 += part1 // 1
# print("остаток: ", part1 % 1)
print(sum1)