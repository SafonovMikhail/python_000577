'''
при введении пары 0-0,
программа завершается досрочно.
'''
i = 0
j = int(input("Введите желаемое число пар чисел: "))
while i < j:
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a==0 and b==0:
        print("программа завершена досрочно")
        break # досрочное завершение цикла
    print(a * b)
    i += 1
if i >= j:
    print("выведено ", i, "пар чисел")