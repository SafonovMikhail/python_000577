words = (input().lower()).split()
count1 = words.count('a') + words.count('an') + words.count('the')
print(f'Общее количество артиклей {count1}')
