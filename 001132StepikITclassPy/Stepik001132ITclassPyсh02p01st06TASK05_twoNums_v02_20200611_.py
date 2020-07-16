a = int(input())
b = int(input())
# a = -27
# b = 12
# a = 27
# b = -12
sigA = (a > 0) - (a < 0)
sigB = (b > 0) - (b < 0)
b1 = (sigA * sigB) * b
print(b1)
