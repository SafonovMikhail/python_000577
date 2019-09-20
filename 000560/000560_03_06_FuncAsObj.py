print("000560_03_06_FuncAsObj.py")

print()
print("000560_03_06_ex01_")
def shout(word):
    return word + "!"
speak = shout
output = speak ("lol")
print(output)

print()
print("000560_03_06_ex01_functions_objects")
# функции как объекты
def myltiply(x,y):
	return x*y
a=4
b=7
operation=myltiply
print (operation(a,b))

print()
print("000560_03_06_task01_functions_var")
# переменной можно назначить функцию
def shout(word):
	return word + '!'
speak=shout
output=speak("lol")
print (output)

print()
print("000560_03_06_ex02_functions_args")
# переменной можно назначить функцию
def add(x,y):
# функция принимает два аргумента, возвращает сумму
	return x + y # 15
# print(do_twice)
def do_twice(func, x,y): # add -> func
# функция do_twice вызывает add
# функция принимает три аргумента
    return func(func(x,y), func(x,y))
# функция принимает 2 аргумента (просто вид двух аргументов)
# Возвращает конкатенацию строк?
a=5
b=10
print ("do_twice(add, a,b):", do_twice(add, a,b))

print()
print("000560_03_06_task02_FuncAsObj")
# Заполнив пропуски, назначьте функцию square в качестве аргумента фукнции test:
def square(x):
    return x*x
def test(func):
    print("square(2):", func)
test(square(2))


