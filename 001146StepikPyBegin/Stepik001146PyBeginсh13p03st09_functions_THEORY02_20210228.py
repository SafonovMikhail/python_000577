'''
Глобальные переменные
'''
birds = 5000  # глобальная переменная


def print_texas():
    print('В Техасе обитает', birds, 'птиц.')


def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')


print_texas()
print_california()
print()

# ----------------------------
print('# глобальная переменная: объявление внутри функции')

birds = 10  #
print(print("[01] birds: до определения фунуций:", birds))


def print_texas():
    global birds  # глобальная переменная.
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')


def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')


birds = 5001  # не работает! Возможно изменить внутри функции.
print("[02] birds: до вызова функции:", birds)
print()
print_texas()
print_california()
print()
print("[03] birds: после вызова функции:", birds)
print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()
