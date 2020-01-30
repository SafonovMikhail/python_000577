'''
с помощью встроенного цикла выводит квадрат из звезд
'''

a = int(input("сколько звезд в строке: "))
for i in range(a):
    for j in range(a):
        print("* ", end="")
    print()

