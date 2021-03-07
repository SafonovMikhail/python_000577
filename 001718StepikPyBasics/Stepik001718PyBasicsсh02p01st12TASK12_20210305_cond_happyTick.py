'''
Антон любит кататься на общественном транспорте и собирать счастливые билеты. Антон живет в крупном городе, в котором билеты имеют шестизначные номера формата ХХХХХХ. Счастливым называется билет, у которого сумма первых трёх цифр равна сумме последних трёх цифр.

Формат входных данных

Натуральное шестизначное число - номер билета, который достался Антону сегодня

Формат выходных данных

Выведите на экран "Ура, повезло!", если Антону достался счастливый билет и "Повезет в следующий раз" в противном случае

Sample Input 1:

123123
Sample Output 1:

Ура, повезло!
Sample Input 2:

123456
Sample Output 2:

Повезет в следующий раз
'''
num1 = input()
# num1 = '123123'
sum1 = 0
sum2 = 0
for i in num1[:3]:
    sum1 += int(i)
# print(sum1)
for j in num1[3:]:
    sum2 += int(j)
# print(sum2)
if sum1 == sum2:
    print('Ура, повезло!')
else:
    print('Повезет в следующий раз')

# из форума (01)
# https://stepik.org/lesson/415334/step/12?discussion=3267558&thread=solutions&unit=404864
n = input()
print("Ура, повезло!" if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(
    n[5]) else "Повезет в следующий раз")

# из форума (02)
# https://stepik.org/lesson/415334/step/12?discussion=3194325&thread=solutions&unit=404864
a = input()
print("Ура, повезло!" if sum([int(a[i]) for i in range(3)]) == sum(
    int(a[i]) for i in range(3, 6)) else "Повезет в следующий раз")

# из форума (03)
# https://stepik.org/lesson/415334/step/12?discussion=3139181&thread=solutions&unit=404864
''' Счастливый шестизначный билет '''
print((lambda b: ["Повезет в следующий раз", "Ура, повезло!"][sum(map(int, b[:3])) == sum(map(int, b[3:]))])(input()))


# из форума (04)
# https://stepik.org/lesson/415334/step/12?discussion=3118504&thread=solutions&unit=404864
def cum(x):
    s = 0
    for i in x:
        s += int(i)
    return s


n = input()
print('Ура, повезло!' if cum(n[:3]) == cum(n[3:]) else 'Повезет в следующий раз')

# из форума (05)
# https://stepik.org/lesson/415334/step/12?discussion=3426724&thread=solutions&unit=404864
def happy_ticket(n):
    n1 = list(map(int,list(n[:3])))
    n2 = list(map(int,list(n[3:])))
    if sum(n1) == sum(n2):
        return "Ура, повезло!"
    return "Повезет в следующий раз"

print(happy_ticket(input()))

