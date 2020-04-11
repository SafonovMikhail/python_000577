import sys, os, time, datetime
# [os] взаимодействие python с операционной системой
# from datetime import datetime

print("sys.platform: ", sys.platform)

# [sys.version] версия python
print("sys.version: ", sys.version)

# [os.getcwd()] - имя папки, в контексте которой выполняется код
print("имя папки с кодом: os.getcwd(): ", os.getcwd())

print("доступ к системным переменным (всем) [os.environ]: ", os.environ)

# пример доступа к конкретной системной переменной
print("PROCESSOR_IDENTIFIER: \t\t\t", os.getenv('PROCESSOR_IDENTIFIER'))

# print(datetime.datetime.today())
print('datetime.date.today(): \t\t\t', datetime.date.today())
print('datetime.date.today().year: \t',datetime.date.today().year)
print('datetime.date.today().month: \t', datetime.date.today().month)
print('datetime.date.today().day: \t\t', datetime.date.today().day)
print('datetime.time(): \t\t\t\t',datetime.time()) # разобраться! Показывает нули
print('time.strftime("%I:%M"): \t\t', time.strftime("%I:%M"))
print('time.strftime("%A %p"): \t\t', time.strftime("%A %p"))
print('datetime.time().minute: \t\t', datetime.time().minute)
print('datetime.date.isoformat(datetime.date.today()): \t', datetime.date.isoformat(datetime.date.today()))

