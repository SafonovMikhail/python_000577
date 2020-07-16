'''
Stepik001132ITclassPyсh02p01st08THEORY02_20200610.py
'''

a, b, c = 'x', 'y', 'z'
print('{} {} {}'.format(a, b, c))

a, b, c = "xyz"
print('{} {} {}'.format(a, b, c))

a, b, c = 1, 2, 3
print('{} {} {}'.format(a, b, c))

a, b, *c, d, e = 1, 2, 3, 4, 5, 6, 7
print('{} {} {} {} {}'.format(a, b, c, d, e))
print(*c,sep='-')

*a, b, c, d, e = 1, 2, 3, 4, 5, 6, 7
print('{} {} {} {} {}'.format(a, b, c, d, e))
print(*a,sep='-')

a, b, c, d, *e = 1, 2, 3, 4, 5, 6, 7
print('{} {} {} {} {}'.format(a, b, c, d, e))
print(*e,sep='*')

#