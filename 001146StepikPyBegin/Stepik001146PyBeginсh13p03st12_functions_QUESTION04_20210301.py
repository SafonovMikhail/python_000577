'''
Что покажет приведенная ниже программа?

x = 5

def add():
    x = 3
    x = x + 5
    print(x)

add()
print(x)
'''
x = 5


def add():
    x = 3
    x = x + 5
    print(x)


add()  # результат выполнения функции - 8 (х+5)
print(x)
