mypass = input()
# mypass = "trustno1_evenurself"
# mypass = "trustno_evenurself"

if "1" in mypass or "2" in mypass or "3" in mypass or "4" in mypass or "5" in mypass or "6" in mypass or "7" in mypass or "8" in mypass or "9" in mypass or "0" in mypass:
    # or ("1234" in mypass) or (
    #     "qwerty" in mypass) or (len(mypass) < 8):
    print("Bad password")
elif "1234" in mypass or "qwerty" in mypass:
    print("Bad password")
# elif "qwerty" in mypass:
#     print("Bad password")
else:
    print("Good password")
