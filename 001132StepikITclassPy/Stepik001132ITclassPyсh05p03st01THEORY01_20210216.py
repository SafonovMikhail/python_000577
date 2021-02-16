string = "1501"
print(string.isdigit())
#True

string = "school"
print(string.isdigit())
#False

string = "sch1501"
print(string.isdigit())
#False

string = "15.01"
print(string.isdigit())
#False

string = "-1501"
print(string.isdigit())
#False

# использование функции

def is_digit(string):
    if string.isdigit():
        return True
    elif string[0] == '-' and string[1:].isdigit(): # проверка на "отрицательность"
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

print(is_digit('school'))
#False

print(is_digit('-1501'))
#True

print(is_digit('-15.01'))
#True

print(is_digit('306'))
#True

print(is_digit('0.05'))
#True

print(is_digit('15.01abc'))
#False

print(is_digit('a.05'))
#False
