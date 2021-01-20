import time
def timechiose():
    import time
    tm1 = time.localtime()
    print("%s-%s-%s %s:%s:%s" % (tm1[2], tm1[1], tm1[0], tm1[3], tm1[4], tm1[5]))
'''
23-07-2020 10:53:44
time.struct_time(tm_year=2020, tm_mon=7, tm_mday=29, tm_hour=13, tm_min=13, tm_sec=54, tm_wday=2, tm_yday=211, tm_isdst=0)
'''
timechiose()
time.localtime()

# import time
# print(time.ctime())
# print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()))
record_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()) # интересная передача значений.
f = open('vybor_igrokov_help.txt', "w") #открываем файл на запись
f.write(record_time + " " + "Игрок 1 выбрал Камень"+"\n") # записываем в файл 1ю строку со временем
f.write(record_time + " " + "Игрок 2 выбрал Ножницы") # записываем в файл 2ю строку со временем
f.close() #закрываем файл — иначе в нем не отобразятся изменения

print("Записано в файл:")
print(record_time + " " + "Игрок 1 выбрал Камень") # записываем в файл 1ю строку со временем
print(record_time + " " + "Игрок 2 выбрал Ножницы") # записываем в файл 2ю строку со временем
print(type(record_time))