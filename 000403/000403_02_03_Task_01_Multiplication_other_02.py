'''
описание оператора [*]
https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
автор: https://stepik.org/users/34866483
'''
a, b , c, d = (int(input()) for i in (1, 2, 3, 4))
print('', *range(c, d+1), sep='\t')
[ print(i, *range(i * c, i * (d + 1), i), sep='\t') for i in range(a, b + 1) ]