print("v01")
a = [int(g) for g in input().split()]
b = 0
for i in a:
    b += i
print(b)

print("v02")
print(sum(int(i) for i in input().split()))

print("v03")
a=[int(i) for i in input().split()]
print(sum(a))

print("v04")
print(sum(map(int, input().split())))

print("v05")
print(eval(input().replace(' ','+')))

print("v06")
a = 0
for i in input().split():
    a += int(i)
print(a)

print("v07")
digits = [int(i) for i in input().split()]
count = 0
summ = 0
while count < len(digits):
    summ += digits[count]
    count += 1
print(summ)



