a, b = (int(input()) for i in (1, 2))
print(((a + (3 - a % 3) % 3) + b - (b % 3)) / 2)
