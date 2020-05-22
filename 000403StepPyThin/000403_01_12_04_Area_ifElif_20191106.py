print("Считаж площади для: \n[прямоугольник], [треугольник], [круг]")
typeFigure = input()
if (typeFigure == 'треугольник'):
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif (typeFigure == 'прямоугольник'):
    a = float(input())
    b = float(input())
    print(a * b)
elif (typeFigure == 'круг'):
    r = float(input())
    print(3.14 * r ** 2)
else:
    print('неизвестная функция')
