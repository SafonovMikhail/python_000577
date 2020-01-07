s = 'aTGcc'
p = 'cc'
print(s.upper())
print(s.lower())
print(s.count(p))
print(s.find(p))
print(s.find('A'))  # выдача -1 означает, что не входит
'''
предпочтительнее использовать
if 'TG' in s
'''
print(s.replace('c', 'C'))
print()
s = 'agTtcAGtc'
print(s.upper().count('gt'.upper()))
