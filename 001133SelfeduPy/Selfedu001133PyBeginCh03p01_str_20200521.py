# способы задания строк
str1 = 'Hello1'
str2 = "Hello2"

# многострочные строки
str3 = '''Многострочные
строки 1''';

str4 = """Многострочные
строки2""";

print(str1)
print(str2)
print(str3)
print(str4)

dig = 5
msg = "число = " + str(dig)
print(msg)

# дубирование строки
one = 'ай '
msg = one * 10
print(msg)

# msg = one * 3.5

# определение длинны строки [len()]
N = len(msg)
print(msg, N)

# проверка наличия подстроки в строке
s = "abcdefg0123"
print("abc" in s)
print('0' in s)
print('43' in s)

# сравнение строк между собой [=]
print("abc" == 'abc')
print("ABC" == 'abc')

# сравнение неравенства строк
psw = "pass"
in_psw = ""
while psw != in_psw:
    in_psw = input("Введите пароль: ")
print("Вход в систему разрешен")

# сравнение строк по величине (лексикографический порядок)

# 