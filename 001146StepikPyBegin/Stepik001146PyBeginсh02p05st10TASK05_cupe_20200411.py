'''
Номер купе
В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом.
Напишите программу, которая определяет номер купе, в котором находится место с заданным номером
(нумерация мест сквозная, начинается с 1).
Формат входных данных
На вход программе подаётся целое число – место с заданным номером в вагоне.
Формат выходных данных
Программа должна вывести одно число – номер купе, в котором находится указаное место.

Stepik001146PyBeginсh02p05st10TASK05_cupe_20200411.py
'''
num = int(input())
print((-1 * num // 4) * -1)
