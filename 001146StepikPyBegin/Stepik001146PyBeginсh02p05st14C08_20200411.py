# мой вариант - левый...
num = int(input())
a = str((num % 10 ** 3) // 10 ** 2)
b = str((num % 10 ** 2) // 10)
c = str(num % 10)
print(a + b + c)
print(a + c + b)
print(b + a + c)
print(b + c + a)
print(c + a + b)
print(c + b + a)
# учебный вариант - основан на изложенном материале
num = int(input())
a = (num % 10 ** 3) // 10 ** 2
b = (num % 10 ** 2) // 10
c = num % 10
print(a, b, c, sep='')
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
