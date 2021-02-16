s = input()
# s = ' name1'
list_stop = [' ', '@', '$', '%']
list_num = '0123456789'
# flag_true = 0
flag_false = 0
for i in list_num:
    if s[0] == i:
        flag_false += 1
        break
for j in s:
    for k in list_stop:
        if j == k:
            flag_false += 1
            break
        else:
            # flag_true += 1
            break
if flag_false >= 1:
    print(False)
else:
    print(True)
