str1 = input()
if str1.find('#') == (-1):
    print(str1)
else:
    print(str1[:str1.find('#')])
