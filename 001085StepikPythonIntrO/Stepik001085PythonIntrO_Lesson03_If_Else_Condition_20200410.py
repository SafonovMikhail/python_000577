# n = int(input())
n = 1200
if n < 10:
    print("Число меньше десяти")
elif n == 10:
    print("Число равно десяти")
elif n > 100:
    print("Число намного больше десяти")
else:
    print("Число больше десяти")

# тернарный оператор
# a = int(input())
# b = int(input())
a = 10
b = 11
res = "Число а больше" if a > b else "Число b больше"
print(res)
