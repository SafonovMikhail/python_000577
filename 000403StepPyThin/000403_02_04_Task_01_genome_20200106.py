gc = input()
count = 0
for i in gc.lower():
    if i == 'g' or i == 'c':
        count += 1
print((count / len(gc)) * 100)
# percent = (count/len(gc))*100
# acggtgttat
# print(gc.upper().count(('g'.upper() or 'c'.upper())))

