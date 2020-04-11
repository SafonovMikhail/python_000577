mypass = input()
if ("1234" or "qwerty" in mypass) or (len(mypass) < 8):
    print("Bad password")
elif ("1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0") not in mypass:
    print("Bad password")
else:
    print("Good password")
