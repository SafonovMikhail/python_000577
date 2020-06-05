'''
Стоимость покупки
Напишите программу, которая считает стоимость трех компьютеров,
состоящих из монитора, системного блока, клавиатуры и мыши.

Stepik001146PyBeginсh02p04st10TASK06_comp_20200411.py
'''
mon = int(input())
sysbl = int(input())
key = int(input())
mouse = int(input())
print((mon + sysbl + key + mouse) * 3)
