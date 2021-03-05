# y = int(input("enter year: "))
y = 2020
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print('ly')
        else:
            print('nly')
    else:
        print('ly')
else:
    print('nly')
