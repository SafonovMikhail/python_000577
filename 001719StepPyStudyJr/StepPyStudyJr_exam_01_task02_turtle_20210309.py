import turtle
import random

# выбор начальных установок
print("Какую фигуру Вы хотите нарисовать (введите цифру)?")
print("[1] - звезда")
print("[2] - треугольник")
print("[3] - квадрат")
print("[4] - шестиугольник")

shape = input()
while True:
    if shape == "1" or shape == "2" or shape == "3" or shape == "4":
        break
    else:
        shape = input("введите корректное значение (от 1 до 4-х) ")
        continue
if shape == '1':  # звезда
    num_sides = 5
    angle = 144
elif shape == '2':  # треугольник
    num_sides = 3
    angle = 120
elif shape == '3':  # квадрат
    num_sides = 4
    angle = 90
elif shape == '4':  # шестиугольник
    num_sides = 6
    angle = 60

print('сколько фигур Вы хотите нарисовать? ')
num_stars = int(input())

print("на каком фоне? [black, green] ")
print("[1] - black")
print("[2] - green")
bckg_clr = input()
while True:
    if bckg_clr == "1" or bckg_clr == "2":
        break
    else:
        bckg_clr = input("введите корректное значение цвета (1 или 2)")
        continue
if bckg_clr == '1':
    bckg_clr = 'black'
else:
    bckg_clr = 'green'

window = turtle.Screen()
turtle.Pen()
turtle.bgcolor(bckg_clr)  # цвет фона
turtle.shape("classic")  # внешний вид черепашки
turtle.speed(0)  # скорость отрисовки

# Список цветов
colors = ['white', 'yellow', 'red', 'blue']
max_index = len(colors) - 1
for i in range(num_stars):  # цикл для заданного количества фигур
    # Random color
    random_index = random.randint(0, max_index)  # выбираем случайный цвет из списка
    new_color = colors[random_index]  # переменной присваиваем значение цвета из списка (по индексу)
    turtle.color(new_color)  # значение цвета помещаем в функцию, отвечающую за цвет в "черепашке"
    turtle.begin_fill()
    for i in range(num_sides):
        turtle.forward(15)
        turtle.right(angle)
    turtle.penup()
    turtle.end_fill()

    # Генерируем фигуры в разных местах экрана
    w = turtle.window_width() // 2 - 50 # 50 - отступ от края экрана
    h = turtle.window_height() // 2 - 50
    x = random.randrange(-w, w)
    y = random.randrange(-h, h)
    turtle.goto(x, y)  # перемещаемся во вновь сгенерированное положение на экране
    turtle.pendown()  # опускаем перо
window.exitonclick()
