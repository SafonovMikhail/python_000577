print("000560_04_02_ExceptionОбработка")

print()
print("000560_04_02_ex.01_ExceptionОбработка")
try:
    # num1 = float(input("Введите первое число: "))
    # num2 = float(input("Введите второе число: "))
    num1 = 1
    num2 = 0
    print("Done calculation:")
    print (num1/num2)
    # print("Done calculation")
except ZeroDivisionError:
    print("an err (zero div)")
except ValueError:
    print("Ошибка! Повторите ввод: введите число")

print()
print("000560_04_02_task.01_ExceptionОбработка")
try:
    var = 10
    print(10/2)
except ZeroDivisionError:
    print("err")
print("finished")

print()
print("000560_04_02_ex.02_ExceptionОбработка")
try:
    var = 10
    print(var + "Hello")
except (ZeroDivisionError, TypeError, ValueError):
    print("err")

print()
print("000560_04_02_task.02_ExceptionОбработка")
try:
    meaning = 42
    print(meaning/0)
    print("The meaning of life")
except (ValueError, TypeError):
    print("VaErr or TyErr!")
except ZeroDivisionError:
    print("div by zero!")

print()
print("000560_04_02_ex.03_ExceptionОбработка")
try:
    word = "spam"
    print(word/0)
except:
    print("err")

print()
print("000560_04_02_task.03_ExceptionОбработка")
try:
    num1 = input(":")
    num2 = input(":")