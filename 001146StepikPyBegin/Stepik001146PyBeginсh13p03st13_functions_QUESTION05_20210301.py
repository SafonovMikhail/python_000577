'''
Что покажет приведенная ниже программа?

x = 5

def add():
    global x
    x = 3
    x = x + 5
    print(x)

add()
print(x)
'''

x = 5

def add():
    global x
    x = 3
    x = x + 5
    print(x)

add()
print(x)