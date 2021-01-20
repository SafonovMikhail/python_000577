####### day08vid01_20:28 ### [open] #######
print("####### day08vid01_20:28 ### [open] #######")
f = open("my_file.txt", "w")  # Кавычки!!!
f.write("hi my file")
f.close()
f1 = open("day8_123.txt")
r = f1.read()
print("day8_123.txt: ")
print(r)

####### day08vid01_17:40 ### [max][min][sum] #######
print("####### day08vid01_17:40 ### [max][min][sum] #######")
s1 = [1231, 1231414, 2352523652356, 34754674, 3452634745687, 56785678956, 34563]
print("max(s1): ", max(s1))
print("min(s1): ", min(s1))
print("sum(s1): ", sum(s1))
print("list(range(0,5)): ", list(range(0, 5)))
print("sum(list(range(0,5))): ", sum(list(range(0, 5))))
print()
####### day08vid01_16:00 ### [range] #######
print("####### day08vid01_16:00 ### [range] #######")
print("range(0,10): ", list(range(0, 10)))
print("range(0,10,2): ", list(range(0, 10, 2)))
print()
####### day08vid01_14:35 ### [len] #######
print("####### day08vid01_14:35 ### [len] #######")
s = "this is my text"
ps = ["1230", 1234, "asldfkjh"]
print(len(s))
print(len(ps))
print()
####### day08vid01_12:56 ### AGE[if] #######
print("####### day08vid01_12:56 ### AGE[if] #######")
print("Введите Ваш возраст: ")
age = input()
if int(age) > 10:  # превращаем в число
    print("Вам больше десяти")
print()
####### day08vid01_11:09 ### [float][int] #######
print("####### day08vid01_11:09 ### [float][int] #######")
print("float: ", float('2.5'))
num1 = int(float('2.5'))
print("int: ", num1)
print()
####### day08vid01_09:52 ### [exec] #######
print("####### day08vid01_09:52 ### [exec] #######")
exec('''a=1
b=2
print(a+b)
''')
print()
####### day08vid01_07:16 ### [eval] #######
print("####### day08vid01_07:16 ### [eval] #######")
eval('''print("Hello eval")''')
print("Введите выражние:")  # варианты: текст, арифметическое выражение,
v = input()
print("Результат: ", eval(v))
# "oleg".upper - вариант для иллюстрации, у меня не проходит в качестве выражения.
print()
####### day08vid01_06-50 ### [upper] #######
print("####### day08vid01_06-50 ### [upper] #######")
s = "hi"
print(s.upper())
print()
####### day08vid01_05-57 ### [help] #######
print("####### day08vid01_05-57 ### [help] #######")
print("описание метода: ", help(s.upper))  # позволяет получить описание метода
print("перевод в верхний регистр: ", s.upper())
print()
####### day08vid01_05-39 ### [dir] #######
print("####### day08vid01_05-39 ### [dir] #######")
s = 'name'
# распечатаем все методы для текстового типа данных
print(dir(s))
list1 = dir(s)
for i in list1:
    print(i)
print("количество методов: ", len(list1))
print()
####### day08vid01_04-05 ### [bool] #######
print("####### day08vid01_04-05 ### [bool] #######")
print(bool(100))  # True
print(bool(-300))  # True
print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False
print(bool("asdl;fashpfgo"))  # True
print()
####### day08vid01_00-00 ### [abs] #######
print("####### day08vid01_00-00 ### [abs] #######")
print(abs(-10))
skorost = -120
if abs(skorost) > 0:
    print("Игрок движется")
# альтернативный вариант (менее рационально)
if skorost > 0 or skorost < 0:
    print("2: Игрок движется")
