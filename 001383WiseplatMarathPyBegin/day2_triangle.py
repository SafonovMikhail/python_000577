a = float(input("введите длинну катета 1 (в см.): "))
b = float(input("введите длинну катета 2 (в см.): "))
c = (a ** 2 + b ** 2) ** 0.5
print("Длина гипотенузы прямоугольного треугольника (в дм.) = ", c / 10)