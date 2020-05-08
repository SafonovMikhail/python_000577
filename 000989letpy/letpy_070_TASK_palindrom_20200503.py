# string = 'А роза упала на лапу Азора'
string = input()
string = string.replace(' ', '').lower()
stringRev = string[::-1]
if stringRev==string:
    print('да')
else:
    print('нет')