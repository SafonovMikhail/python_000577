import string


def onlyletters(s):
    s1 = []
    for i in s:
        if i not in string.punctuation:  # проверяем посимвольно, есть ли в списке пунктуационных знаков
            s1.append(i)
    s2 = ''.join(s1)  # соединяем массив символов в слово
    return s2


words = (input().lower()).split()  # преобразуем слова на этапе ввода
words_opt = []  # создаем оптимизированный список
for item in words:
    words_opt.append(onlyletters(item))

count1 = words_opt.count('a') + words_opt.count('an') + words_opt.count('the')
print(f'Общее количество артиклей {count1}')

# my_02
words = (input().lower()).split()
count1 = words.count('a') + words.count('an') + words.count('the')
print(f'Общее количество артиклей {count1}')

# f01
print('Общее количество артиклей:', sum([1 for i in input().split() if i.lower() in ('a', 'an', 'the')]))

# f2
print('Общее количество артиклей:', len([i for i in input().split() if i.lower() in ('a', 'an', 'the')]))

# f3
print(f"Общее количество артиклей: {len([i for i in input().split() if i.lower() in ['a', 'an', 'the']])}")

# f4
s = input().lower().split()
count = [s.count('a'), s.count('an'), s.count('the')]
count = sum(count)
print(f'Общее количество артиклей: {count}')

# f5
ss = input().lower().split()
print('Общее количество артиклей:', sum(ss.count(article) for article in ('a', 'an', 'the')))

# f6
s, cnt = input().lower().split(), 0
articles = ['a', 'an', 'the']
for word in s:
    if word in articles:
        cnt += 1
print("Общее количество артиклей:", cnt)

# f7
# put your python code here
l = input().lower()
count = 0
for i in l.split(' '):
    if i == 'a' or i == 'an' or i == 'the':
        count += 1
print('Общее количество артиклей:', count)

# f8
from re import findall

txt = input().lower()
res = findall(r'\ba\b|\ban\b|\bthe\b', txt)
print(f"Общее количество артиклей: {len(res)}")

# f9

