s = "Hello! This is my new game\
Guess my number"
print(s)  # Hello! This is my new game Guess my number

# работа со строками
print("Start:\n\tstring\n\tstring\n\tstring\nEnd")
print()

s1 = "Hello"
s2 = "World"
print(s1 + s2)  # HelloWorld

s1 = "Hello"
print(s1 * 3)  # HelloHelloHello
print()

# индексация строк
s = "Hello World"
print(s)
print("symbol [0]: " + str(s[0]))  # H
print("symbol [6]: " + str(s[6]))  # W

# методы строк
s = "guEss mY numBer"
print(s)
s.capitalize()  # Guess my number
s.title()  # Guess My Number
s.upper()  # GUESS MY NUMBER
s.lower()  # guess my number
print(s)
s1 = s.capitalize()  # Guess my number
s2 = s.title()  # Guess My Number
s3 = s.upper()  # GUESS MY NUMBER
s4 = s.lower()  # guess my number
print(s1, s2, s3, s4, sep='; ')

# Метод find и rfind
s = "message"
s.find("m")  # 0
s.find("s")  # 2
s.find("w")  # -1

s = "message"
s.rfind("m")  # 0
s.rfind("s")  # 3
s.rfind("w")  # -1

# replace
s = "best regards best"
print(s)
s.replace("best", "kind")  # kind regards kind
s1 = s.replace("best", "kind")  # kind regards kind
print('s1:', s1)
s.replace("best", "kind", 1)  # kind regards best
s2 = s.replace("best", "kind", 1)  # kind regards best
print('s2:', s2)
print(s)

# Метод count
s = "Hello World"
s4 = s.count("l")  # 3
print(s4)

# Методы строк
password = "qw@E1r"
print("\nTry isalpha: ")
for symbol in password:
    alpha = symbol.isalpha()
    print(f"{symbol} - {alpha}")
    if (not alpha) and (symbol == "@"):
        print(f"It is {symbol}")

# Срезы строк
s = "message"
print(s[0:])  # message
print(s[2:5])  # ssa
print(s[2:-1])  # ssag
print(s[1:6:2])  # esg
print(s[:5])  # messa
print(s[:])  # message

# надежный пароль
import random

s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2 = "0123456789"
s3 = "~!@#$%^&*()_+{}[\]:/-"
s = s1.lower() + s1.upper() + s2 + s3
for i in range(15):
    p = random.choice(s)
    print(p, end='')
print()

# модуль string
import string

s1 = string.ascii_letters
# s1 = string.printable
s2 = string.digits
s3 = string.punctuation
s = s1 + s2 + s3
for i in s:
    print(i, end='')
