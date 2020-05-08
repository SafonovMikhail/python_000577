#ex001_sum_2019-05-22.py
# print(float(input("input 1st number: "))+float(input("input 2nd number: ")))
# input()

n = 50
s = 0
while s <= 249:
    s = s + 24
    n = n + 5
print(n)

n = 0
s = 0
while s <= 257:
    s = s + 25
    n = n + 2
print(n)


a = 25
b = 12
a = 3 * b - a # 36-25=11
if a > b:
    c = 2 * a - b
else:
    c = 2 * a + b #22+12
print(c)