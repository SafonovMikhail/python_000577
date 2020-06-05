from datetime import datetime #модуль [datetima], подмодуль [datetime]
# импортирует функциональность(?) из стандартной библиотеки
from os import getcwd
# getwcd - это что?
import sys
import os

# import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57,
        59]
right_this_minute = datetime.today().minute
print("\nright_this_minute: ",right_this_minute)
if right_this_minute in odds:
    print("\nodd minute")
else:
    print("\neven minute")

where_am_I = getcwd()
print("\ngetcwd() - возвращает имя текущего каталога:" )
# print("\n", where_am_I)
print(where_am_I)

print("\nsys: модуль для...")
print("\nsystem(sys.platform): ", sys.platform)
print("\nPythonVersion(sys.version): ", sys.version)

print (os.getcwd())
# [getcwd] – возвращает текущий рабочий каталог

print("\nEnvironment(os.environ): ", os.environ)
print("доступ ко всем переменным окружения")

print("\nEnvironment os.getenv('PATH'): ", os.getenv('PATH'))
# [getenv] – возвращает конкретную переменную окружения

print("\nEnvironment os.getenv('APPDATA'): ", os.getenv('APPDATA'))

print("\nEnvironment os.getenv('HOME'): ", os.getenv('HOME'))
# не отмечено, для чего это нужно [20200530]





