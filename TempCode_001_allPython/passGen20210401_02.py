import datetime
import base64
import random


def Revers(string):
    string = string[::-1]
    return string


def CorrectPass(password):
    for x in password:
        password = password.replace(x, "")
        if len(password) == passwordlen:
            break
    return password


# Get data
timer = datetime.datetime.now()
# Morph str
timer = str(timer)
timer = timer.replace('-', '')
timer = timer.replace(' ', '')
timer = timer.replace(':', '')
timer = timer.replace('.', '')
# Revers or not
realrandom = random.choice([1, 2])
if realrandom == 1:
    timer = Revers(timer)
# Encode str
timer = base64.b64encode(bytes(timer, "utf-8"))
# Morph
timer = str(timer)
timer = timer.replace("b'", "")
timer = timer.replace("='", "")
# Len
passwordlen = 20  # Change this
if passwordlen != len(timer):
    timer = CorrectPass(timer)
# Check
while True:  # Если в выводе ничего не получили, то запустите скрипт еще раз, до тех пор пока не получите.
    if timer == '':
        timer = CorrectPass(timer)
    break
print(timer)
