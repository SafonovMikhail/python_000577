'''
Количество совпадающих пар
На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести одно число – количество пар элементов, равных друг другу.

Sample Input 1:

1 7 5 7 5
Sample Output 1:

2
Sample Input 2:

3 3 3 3 3
Sample Output 2:

10
Sample Input 3:

8 7 6
Sample Output 3:

0
'''
s = input()
s1 = s.split(" ")
count = 0
for i in range(len(s1) - 1):  # !!!
    for j in range(i + 1, len(s1)):
        if s1[i] == s1[j]:
            count += 1
print(count)

# v.01 (Ренат Хабибуллин)
a = input().split()
s = 0
for i in range(len(a) - 1):
    s += a[i + 1:].count(a[i])
print(s)

# v.02
nums, pairs = input().split(), 0
for i in range(len(nums)):
    pairs += nums.count(nums[i]) - 1
print(pairs // 2)

# v.03
a = input().split()
print(sum(a.count(x) - 1 for x in a) // 2)

# v.04
a = input().split()
p = 0
for i in range(len(a)):
    p += a[i::].count(a[i]) - 1
print(p)

# v.05
# https://stepik.org/lesson/324755/step/9?discussion=3313192&thread=solutions&unit=307931
s = input().split()
special_list = []
for i in range(len(s)):
    if s[i] not in special_list:
        special_list.append(s[i])
pairs = []
for digit in special_list:
    new_pair = s.count(digit)
    if new_pair > 1:
        pairs.append(new_pair)
from math import *

result = 0
for pair in pairs:
    f = pair - 2
    result += (factorial(pair)) / (2 * (factorial(f)))
print(int(result))

# v.06
# https://stepik.org/lesson/324755/step/9?discussion=3205638&thread=solutions&unit=307931
x, y, cnt, k = input().split(), [], 0, 0
for i in x:
    if x.count(i) >= 2 and i not in y:
        y.append(i)
        cnt = x.count(i) * (x.count(i) - 1) // 2
        k += cnt
print(k)

# v.07
# https://stepik.org/lesson/324755/step/9?discussion=3114307&reply=3116586&thread=solutions&unit=307931
numbers, count = input().split(), 0
for i in range(len(numbers)):
    x, numbers[i] = numbers[i], ' '
    count += numbers.count(x)
print(count)

# v.08
# https://stepik.org/lesson/324755/step/9?discussion=1846262&thread=solutions&unit=307931
from collections import Counter
cnt = Counter(map(int, input().split()))
print(sum(c*(c-1)//2 for c in cnt.values()))

# v.09
# https://stepik.org/lesson/324755/step/9?discussion=1846194&thread=solutions&unit=307931
l = [int(x) for x in input().split()]
print((sum([1 for x in l for y in l if x == y]) - len(l)) // 2)

# v.10
# https://stepik.org/lesson/324755/step/9?discussion=1613532&thread=solutions&unit=307931
import itertools
n = [int(i) for i in input().split()]
print(len([i for i in itertools.combinations(n,2) if i[0] == i[1]]))

# v.11
# https://stepik.org/lesson/324755/step/9?discussion=1613532&thread=solutions&unit=307931
from math import factorial as fk

kol_par = 0
m = 2
num1 = list(map(int, input().split()))
num2 = set(num1)
for i in num2:
    n = num1.count(i)
    if n >= m:
        c = fk(n) / (fk(m) * fk(n - m))
        kol_par += c
print(int(kol_par))

# v.12
# https://stepik.org/lesson/324755/step/9?discussion=1591743&thread=solutions&unit=307931
a = input().split()
n = 0

while True:
    k = a.count(a[0])
    if k >= 2:
        n += k - 1
    del a[0]
    l = len(a)
    if l == 0:
        break
print(n)


# v.13
# https://stepik.org/lesson/324755/step/9?discussion=3474565&thread=solutions&unit=307931
lst = list(map(int, input().split()))
print(sum([lst[i] == lst[j] for i in range(len(lst) - 1) for j in range(i + 1, len(lst))]))

# v.14
# https://stepik.org/lesson/324755/step/9?discussion=3461498&thread=solutions&unit=307931
lst = list(map(int, input().split()))
print(sum(lst[i + 1:].count(j) for i, j in enumerate(lst)))

# v.15
# https://stepik.org/lesson/324755/step/9?discussion=3459811&thread=solutions&unit=307931
s = list(map(int, input().split()))
cont = 0
for i, n in enumerate(s):
    for j in range(i + 1, len(s)):
        if n == s[j]:
            cont += 1
print(cont)

# v.16
# https://stepik.org/lesson/324755/step/9?discussion=3442066&thread=solutions&unit=307931
counter = 0
input_data = input()
numbers = input_data.split()
already_counted_numbers =[]
for i in range(len(numbers)):
    if numbers[i] not in already_counted_numbers:
        counter += numbers.count(numbers[i]) * (numbers.count(numbers[i]) - 1 ) // 2
        already_counted_numbers.append(numbers[i])
print(counter)

# v.17
# https://stepik.org/lesson/324755/step/9?discussion=3428140&thread=solutions&unit=307931
arr = input().split()
res = 0
for i in range(len(arr)):
    if arr.count(arr[i]) > 1 and arr[i] != '+':
        res += arr.count(arr[i]) - 1
        arr[i] = '+'
print(res)

# v.18
# https://stepik.org/lesson/324755/step/9?discussion=3421904&thread=solutions&unit=307931
a = input().split()
counter = 0

for i in a:
    for j in a:
        if i == j:
            counter += 1

print((counter-len(a))//2)

# v.19
# https://stepik.org/lesson/324755/step/9?discussion=3415335&thread=solutions&unit=307931
a = [int(s) for s in input().split()]
count = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            count += 1
print(count)


# v.20
# https://stepik.org/lesson/324755/step/9?discussion=3411941&thread=solutions&unit=307931
lst = input().split()
cnt = 0
for i in lst:
    for j in lst[lst.index(i) + 1::]:
        if int(i) == int(j):
            cnt = cnt + 1
print(int(cnt / 2))

# v.21
# https://stepik.org/lesson/324755/step/9?discussion=3400715&thread=solutions&unit=307931

ints = [int(i) for i in input().split()]
sum = 0
for i in range(len(ints)):
    current_element = ints[i]
    sub_arr = ints[i + 1:]
    sum += sub_arr.count(current_element)
print(sum)

# ints = [int(i) for i in input().split()]
# print(sum([ints[i + 1:].count(ints[i]) for i in range(len(ints))]))

# v.22
# https://stepik.org/lesson/324755/step/9?discussion=3389124&thread=solutions&unit=307931
a = list(map(int,input().split()))
lst = []
suma = 0
for i in range(10):
    if a.count(i) > 1:
        lst.append(a.count(i))
for j in range(len(lst)):
    while lst[j] > 1:
        suma += lst[j] - 1
        lst[j] -= 1
print(suma)

# v.23
# https://stepik.org/lesson/324755/step/9?discussion=3379278&thread=solutions&unit=307931
s = input().split()
total = 0
for n in range(len(s)):
    total += s[n + 1:].count(s[n])
print(total)

# v.24
# https://stepik.org/lesson/324755/step/9?discussion=3379272&thread=solutions&unit=307931
import math
numbers = [int(x) for x in input().split()]
counter = 0
for i in set(numbers):
    x = numbers.count(i)
    if x > 1:
        counter += math.factorial(x)/math.factorial(x - 2)/2
print(round(counter))

# v.25
# https://stepik.org/lesson/324755/step/9?discussion=3372580&thread=solutions&unit=307931
s = input().split()
sl = list(set(s))
total = 0

for k in sl:
    if k in s:
        c = s.count(k)
        total += (int(c * (c - 1) / 2))
print(total)

# v.26
# https://stepik.org/lesson/324755/step/9?discussion=3368594&thread=solutions&unit=307931
lst = input().split()
cnt = 0
for i in range(len(lst) - 1):
    j = i + 1
    while j <= len(lst) - 1:
        if lst[i] == lst[j] and i != j:
            cnt += 1
        j += 1
print(cnt)

# v.27


