# x = int(input())
x = 14213412345234623456245
digits = []
# обратный порядок
while x:
    digits.append(x % 10)
    x = x // 10
print(digits)

# прямой порядок
x1 = 14213412345234623456245
digits = []
while x1:
    digits = [x1 % 10] + digits  # конкатенация?
    # digits = digits + [x1 % 10]  # конкатенация?

    x1 = x1 // 10
print(digits)
