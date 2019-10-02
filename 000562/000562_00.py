from datetime import datetime
from os import getcwd
import sys
import os

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57,
        59]
right_this_minute = datetime.today().minute
print("\n",right_this_minute)
if right_this_minute in odds:
    print("\nodd.")
else:
    print("\nnot an odd minute")

where_am_I = getcwd()
print("\n", where_am_I)

print("\nsystem: ", sys.platform)
print("\nPythonVersion: ", sys.version)
print("\nEnvironment: ", os.environ)






