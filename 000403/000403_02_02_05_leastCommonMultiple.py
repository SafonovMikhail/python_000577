a = int(input())
b = int(input())
# наибольший общий делитель
if a < b:
    a, b = b, a
i = 2
while (a % i != 0 and b % i != 0):
    print(i)
    i += 1
