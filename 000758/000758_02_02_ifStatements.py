# 000758_02_02_ifStatements.py

print("000758_02_02_ifStatements:01")
if 10 > 5:
    print("10 greater than 5")
print("Program ended")
print("")
print("000758_02_02_ifStatements:02:nested")
num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 5 and 47")
print("")
print("000758_02_02_ifStatements:q.03:nested")
num = 7
if num > 3:
    print("3")
    if num < 5:
        print("5")
        if num == 7:
            print("7")
print("")
print("000758_02_02_ifStatements:q.03:nested:reorganized ")
num = 7
if num > 3:
    print("3")
    if num < 5:
        print("5")
        if num == 7:
            print("7")
print("")
num = 7
if num > 3:
    print("3")
    if num < 5:
        print("5")
    if num == 7:
        print("7")
