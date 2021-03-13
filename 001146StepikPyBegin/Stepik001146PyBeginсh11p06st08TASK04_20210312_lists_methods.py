'''
Взлом Братства Стали 🌶️
Немалоизвестный в пустошах Мохаве Курьер забрел в Хидден-Вэли – секретный бункер Братства Стали, и любезно соглашается помочь им в решении их проблем. Одной из такой проблем являлся странный компьютерный вирус, который проявлялся в виде появления комментариев к программам на терминалах Братства Стали. Известно, что программисты Братства никогда не оставляют комментарии к коду, и пишут программы на Python, поэтому удаление всех этих комментариев никак не навредит им. Помогите писцу Ибсену удалить все комментарии из программы.

Формат входных данных
На первой строке вводится символ решётки и сразу же натуральное число nn — количество строк в программе, не считая первой. Далее следует nn строк кода.

Формат выходных данных
Нужно вывести те же строки, но удалить комментарии и символы пустого пространства в конце строк. Пустую строку вместо первой строки ввода выводить не надо.

Sample Input:

#12
print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")    # ахахахах вам не поймать меня
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)         #долой Макнамару
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)          #Элайджа вперёд
else:
    print("Здравствуйте, послушник", name)
Sample Output:

print("Введите своё имя")
name = input()
print("Введите пароль, если имеется")
password = input()
if password == "hoover":
    print("Здравствуйте, рыцарь", name)
elif password == "noncr":
    print("Здравствуйте, паладин", name)
elif password == "gelios":
    print("Здравствуйте, старейшина", name)
else:
    print("Здравствуйте, послушник", name)
'''

# Гуев
n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())

# @Михаил, входные данные: #6 kdeaefk                           #tndjwd awk()()!!!...

# f01
# https://stackoverflow.com/questions/904746/how-to-remove-all-characters-after-a-specific-character-in-python
print(*map(lambda i: i.split('#')[0].rstrip(), __import__('sys').stdin.read().splitlines()[1:]), sep='\n')

# f02
n = input().split('#')
for i in range(int(n[1])):
    print(input().split('#')[0].rstrip())

# f03
[print(input().split('#')[0].rstrip()) for _ in range(int(input()[1:]))]

# f05
n, li = input(), []
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')].rstrip()
    li.append(s)
print(*li, sep='\n')

# f06
n = int(input()[1:])

for i in range(n):
    line = input().split('#')
    line = line[0].rstrip()
    print(line)

# f07
for i in range(int(input().replace('#', ''))):
    li = (input().split('#', 1))
    print(li[0].rstrip())

# f08
N = int(input().split('#')[-1])
for i in range(N):
    S = input().split('#')
    print(S[0].rstrip())

# f09
n = int(input().split('#')[1])
for _ in range(n):
    print(input().split('#')[0].rstrip())

# f10
n = int(input()[1:])
for i in range(n):
    s = input()
    m = []
    b = 0
    while s[b] == ' ':
        m.append('')
        b += 1
    m.extend(s.split())
    for w in m:
        if w == '':
            continue
        elif w[0] == '#':
            a = m.index(w)
            while a < len(m):
                del m[a]

    print(*m)

# f11
n = int(input()[1:])
for _ in range(n):
    s = input().split('#')
    print(s[0].rstrip())

# f12
n = int(input().replace('#', ''))
lst = []
for _ in range(n):
    lst.append(input().split('#')[0].rstrip())
print(*lst, sep='\n')

# f13
for _i in range(int(input()[1:])):
    print(input().split('#')[0].rstrip())

# f14
numbers = input()
amount_rows_str = ''
for i in numbers:
    if i.isdigit():
        amount_rows_str += i
    else:
        continue
amount_rows_int = int(amount_rows_str)
for j in range(amount_rows_int):
    row = input()
    if "#" in row:
        row_list = row.split("#")
        del row_list[-1]
        print(row_list[0].rstrip())
    else:
        row_list = []
        row_list.append(row)
        print(row_list[0].rstrip())

# f15
n = input()
n = n.replace('#', '')
for i in range(int(n)):
    string = input()
    if '#' in string:
        a = string.rfind('#')
        string = string[:a]
    print(string.rstrip())

# f16
n = int(input()[1:])
for _ in range(n):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())

# f17
[print((lambda a: a[:a.index("#") if "#" in a else None].rstrip())(input())) for _ in range(int(input()[1:]))]

# f18
n=int(input()[1:])
for i in range(n):
  a=input().split('#')
  print(a[0].rstrip())

# f19
s = input()
x = []
string = ''
for i in range(int(s[1:])):
    x = input()
    for j in range(len(x)):
        if '#' in x[j]:
            string += x[:x.index('#')].rstrip() + '\n'
            break
    else:
        string += x.rstrip() + '\n'
print(string)


# f20
n = int(input()[1:])
code = []

for _ in range(n):
    string = input().split('#')[0].rstrip()
    code.append(string)

print(*code, sep='\n')

# f21
h, l = input(), []
n = int(h[1:])

for i in range(n):
    s = input().split('#')
    l.append(s[0].rstrip())

print(*l, sep='\n')

# f22
print(*[input().split('#')[0].rstrip() for _i in range(int(input().lstrip('#')))], sep='\n')

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01

# f01
