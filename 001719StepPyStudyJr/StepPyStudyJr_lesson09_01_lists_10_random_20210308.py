import random

stats = []
attributes = 5
print('Stats: ', end='')
for i in range(attributes):
    r = random.randint(40, 70)
    stats.append(r)
    print(stats[i], end=' ')
print('\n\t[1] - Strength\
        \n\t[2] - Dexterity\
        \n\t[3] - Intelligence\
        \n\t[4] - Wisdom\
        \n\t[5] - Charisma')
select = int(input('Select: '))
select -= 1
stats[select] = stats[select] + random.randint(5, 10)
for i in range(len(stats)):
    if i == select:
        continue
    stats[i] = stats[i] - random.randint(5, 10)
print('Stats: ', end='')
for i in range(attributes):
    print(stats[i], end=' ')
