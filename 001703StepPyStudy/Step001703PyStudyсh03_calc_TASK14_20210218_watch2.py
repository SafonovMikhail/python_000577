'''
Задача «Часы - 2»
Условие
С начала суток часовая стрелка повернулась на угол в α градусов. Определите на какой угол повернулась минутная стрелка с начала последнего часа. Входные и выходные данные — действительные числа.
'''
a = float(input())
# a = 0.5
print((a % 30) * 12)
