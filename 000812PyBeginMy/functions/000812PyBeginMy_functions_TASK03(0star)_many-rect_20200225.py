'''
произвольное количество прямоугольников
'''


def rect():
    for i in range(5):
        print('*' * 5)


n = int(input('Введите количество прямоугольников: '))
for i in range(1, n + 1):
    print(i)
    rect()
