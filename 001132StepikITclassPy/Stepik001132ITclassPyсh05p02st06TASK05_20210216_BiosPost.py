'''
Начальная загрузка — сложный и многошаговый процесс запуска компьютера. Один из таких шагов, когда программа инициализации BIOS с помощью программы POST проверяет, что устройства компьютера работают корректно и инициализирует их. В большинстве персональных компьютеров в случае успешного прохождения POST системный динамик издаёт один короткий звуковой сигнал beep, в случае сбоя — различные последовательности звуковых сигналов, позволяющие определить причину неисправности. Напиши программу на вход которой подается строка, если в этой строке встречается слово "beep", то твоя программа должна вывести "FF" (код  загрузки операционной системы), иначе "00" ("нулевой" этап загрузки).

Sample Input 1:

Если при включении из компьютера слышно: beeeeeep beeeeeep beeeeeep, то это неисправна материнская плата (ошибка контроллера клавиатуры).
Sample Output 1:

00
Sample Input 2:

Если при включении сигнал из компьютера beeeeeee... (непрерывный), то это проблемы с блоком питания или материнской платой.
Sample Output 2:

00
Sample Input 3:

Если при включении сигнал из компьютера beep, то это успешный POST и продолжение загрузки компьютера.
Sample Output 3:

FF
'''
s1 = input()
signal = 'beep'
if signal in s1:
    print('FF')
else:
    print('00')
