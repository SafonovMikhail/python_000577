'''
Сортировка чисел
На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел. Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.

Формат входных данных
На вход программе подается строка текста, содержащая целые числа, разделенные символом пробела.

Формат выходных данных
Программа должна вывести две строки текста в соответствии с условием задачи.

Sample Input:

4 5 1 2 3 8
Sample Output:

1 2 3 4 5 8
8 5 4 3 2 1
'''
s = input().split(' ')
s_num = []
for i in s:
    s_num.append(int(i))

s_num.sort()

s1 = []
for _ in s_num:
    s1.append(_)

s_num.sort(reverse=True)

s2 = []
for _ in s_num:
    s2.append(_)

s1_str = []
for i in s1:
    s1_str.append(str(i))

s2_str = []
for i in s2:
    s2_str.append(str(i))

print(' '.join(s1_str))
print(' '.join(s2_str))

# f1
n = input().split()  # считываем данные
for i in range(len(n)):  # запускаем цикл
    n[i] = int(n[i])  # преобразуем строковые данные в цифровые
n.sort()  # сортируем список
print(*n)  # выводим на печать 1-ую строку
n.sort(reverse=True)  # переворачиваем отсортированный список
print(*n)  # выводим на печать 2-ую строку

# f2
s = sorted(int(i) for i in input().split())
print(*s)
print(*s[::-1])

# f3
m = [int(i) for i in input().split()]
m.sort()
print(*m)
m.reverse()
print(*m)

# f4
n = input().split()
n.sort(key=int)
print(*n)
n.sort(reverse=True, key=int)
print(*n)

# f5
n = [int(_) for _ in input().split()]
n.sort()
print(*n)
n.sort(reverse=True)
print(*n)

# f6
n = [int(_) for _ in input().split()]
n.sort()
print(*n)
n.sort(reverse=True)
print(*n)

# f7
digits = [int(i) for i in input().split()]
print(*sorted(digits))
print(*sorted(digits, reverse=True))

# f8
l = [int(i) for i in input().split()]
l.sort()
print(*l)
l.sort(reverse=1)
print(*l)

# f9
spisok = list(map(int, input().split()))
print(*sorted(spisok))
print(*sorted(spisok, reverse=True))

# f10
nums = [int(x) for x in input().split()]
print(*sorted(nums))
print(*sorted(nums, reverse=True))

# f11
a = input()
a = a.split()
n = []
for i in range(len(a)):
    n.append(int(a[i]))
n.sort()
print(*n)
n.sort(reverse=True)
print(*n)

# f12
s = input().split()
h = []
g = []
for i in s:
    h.append(int(i))
    g.append(int(i))
    h.sort()
    g.sort(reverse=True)

print(*h)
print(*g)

# f13
line = [int(num) for num in input().split()]
print(' '.join(map(str, sorted(line))))
print(' '.join(map(str, sorted(line, reverse=True))))

# f14
lst = list(map(str, sorted(map(int, input().split()))))
print(' '.join(lst), '\n', ' '.join(lst[::-1]), sep='')

# f15
s = list(map(int, input().split()))
s.sort()
print(*s)
s.sort(reverse=True)
print(*s)

# f16
a = sorted(list(map(int, input().split())))
print(*a)
print(*reversed(a))

# f17
text = input().split()
for i in range(len(text)):
    text[i] = int(text[i])
text.sort()
print(*text, sep=' ')
text.sort(reverse = True)
print(*text, sep=' ')

# f18
a = sorted(input().split(), key=lambda x: int(x))
print(' '.join(a), ' '.join(a[:: -1]), sep='\n')

