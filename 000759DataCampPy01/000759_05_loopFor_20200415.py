# 000759_05_loopFor.py

# последнее значение не входит в диапазон
for num in range(1, 5):
    # параметры функции print()
    print(num, end='*')

print()
print()
for num2 in range(100, 102):
    print("@@ num2")
    for num3 in range(2):
        print("num3 @@@")

print()
print(num, sep="")
print(num, sep="sep@@@ ")

print()
print()
print("for num in range(1, 4): ")
for num in range(1, 4):
    print(num)

print()
print("num: ", num, sep="", end="~")
print("num: ", num, sep="sep@@@@ ")

print()
print()
print("for num in range(1, 10): ")
for num in range(1, 10):
    print(num)

print("num: ", num, sep="")
print("num: ", num, sep="sep@@@@@ ", end="~~~~")

'''
что мы можем сказать о фукнции print()?
По умолчанию у нее есть некоторые параметры.
В конце фукнции, что она выводит? - перевод строки
как правило, мы хотим перевести строку.

по умолчанию также не обозначен параметр "step()"
'''
