n = int(input())
wlist = []
wlist.append(input())
for i in range(n - 1):
    new_item = input()
    wlist.append(new_item)
    for j in range(len(wlist)-1):
        if wlist[j] == new_item:
            del wlist[-1]
print(wlist)