'''
10 прямоугольников
'''


def rect():
    for i in range(5):
        print("*" * 5)


count = 0
for i in range(10):
    count += 1
    print(count)
    rect()
