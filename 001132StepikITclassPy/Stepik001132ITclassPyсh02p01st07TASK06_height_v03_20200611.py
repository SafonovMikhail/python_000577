'''
https://www.programmersforum.ru/showthread.php?p=1816458#post1816458
+ пояснения по синтаксису
'''
h1 = int(input())
h2 = int(input())
h3 = int(input())
print(['Не по росту!', 'По росту.'][h1 <= h2 <= h3])