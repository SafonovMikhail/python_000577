found = []
print(len(found))
found.append('a')
print(len(found))
found.append('e')
found.append('i')
found.append('o')
print(len(found))
print('')
# печать списка
for i in found:
    print(i)
# [not in] - команда по проверке отсутствия элемента
if 'u' not in found:
    found.append('u')
print('')
print(found)