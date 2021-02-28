print()

# ----------------------------
print('# ')


def draw_box(height, width):  # функция принимает два параметра
    for i in range(height):
        print('*' * width)


draw_box(10, 100)
print()

# ----------------------------
print('# прямоугольники разных размеров:')
draw_box(3, 3)
print()
draw_box(5, 5)
print()
draw_box(4, 10)
print()

# ----------------------------
print('# параметры - переменные')
n = 3
m = 9
draw_box(n, m)
print()

# ----------------------------
print('# параметры - переменные 02:')
def print_hello(n):
    print('Hello' * n)

print_hello(3)
print_hello(5)
times = 2
print_hello(times)
print()

# ----------------------------
print('# функция: два параметра')
def print_text(txt, n):
    print(txt * n)

print_text('Hello', 5)
print_text('A', 10)
print()

# ----------------------------
print('# функции: аргументы. параметры')
def draw_box(height, width):
    for i in range(height):
        print('*' * width)
# параметрами являются переменные height и width.

# В момент вызова функции draw_box(height, width):
# аргументами являются height и 9.
height = 10
draw_box(height, 9)
print()

# ----------------------------
print('# функции: внесение изменений в переменные.')
def draw_box(height, width):
    height = 2
    width = 10
    for i in range(height):
        print('*' * width)

n = 5
m = 7
draw_box(n, m)
print(n, m)
print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

