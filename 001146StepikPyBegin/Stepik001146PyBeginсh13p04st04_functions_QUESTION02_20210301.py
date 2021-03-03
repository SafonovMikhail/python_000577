'''
Функция do_something() определена следующим образом:

def do_something(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result
Что будет выведено в результате выполнения следующего программного кода?

print(do_something([2, 2, 2, 2]))
'''


def do_something(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result


print(do_something([2, 2, 2, 2]))
