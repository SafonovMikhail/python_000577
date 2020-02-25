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
print("PROCESSOR_IDENTIFIER: ", os.getenv('PROCESSOR_IDENTIFIER'))

# print(datetime.datetime.today())
# print("datetime.date.today(): ", datetime.date.today())
# print(datetime.date.today().year)
# print(datetime.date.today().month)
# print(datetime.date.today().day)
# print(datetime.time())
# print('datetime.date.isoformat(datetime.date.today()): ', datetime.date.isoformat(datetime.date.today()))
print('time.strftime("%I:%M"): ', time.strftime("%I:%M"))
print('time.strftime("%A %p"): ', time.strftime("%A %p"))
print('datetime.time().minute: ', datetime.time().minute)

