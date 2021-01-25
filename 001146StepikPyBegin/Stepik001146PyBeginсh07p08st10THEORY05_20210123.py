'''
Задача 2. Найдите все пары натуральных чисел (и их количество) являющихся
решением уравнения x^2+y^2+z^2 = 2020
'''
# предварительные вычисления: x,y,z <= 45
count = 0
for x in range(1, 45):
    for y in range(1, 45):
        for z in range(1, 45):
            if x ** 2 + y ** 2 + z ** 2 == 2020:
                print(f"{x}:{y}:{z}")
                count += 1
print(count)
