num = int(input())
d1 = (num % 10 ** 3) // 10 ** 2
d2 = (num % 10 ** 2) // 10
d3 = num % 10
print("Сумма цифр =", d1 + d2 + d3)
print("Произведение цифр =", d1 * d2 * d3)
