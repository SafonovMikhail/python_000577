string = input()
string_length = len(string)
print(string_length)

string = input()
if len(string) < 5:
    print("Ошибка! Введите больше пяти символов!")

string = input()
if not string:
    print("Ошибка! Введите хоть что-нибудь!")

string = input()
if len(string) == 0:
    print("Ошибка! Введите хоть что-нибудь!")
