s = 'aTGcc'
p = 'cc'
print('01: ', s.upper())
print('02: ', s.lower())
print('03: ', s.count(p))
print('04: ', s.find(p)) # почему? (место вхождения)
print('05: ', s.find('A'))  # выдача -1 означает, что не входит
'''
предпочтительнее использовать
if 'TG' in s
'''
print('06: ', s.replace('c', 'C'))
print()
s = 'agTtcAGtc'
print('07: ', s.upper().count('gt'.upper()))
print('08: ', s.upper())
print('09: ', 'gt'.upper())
print('10: ', s)

