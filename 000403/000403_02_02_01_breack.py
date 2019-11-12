i = 0
s = 0
while i < 5:
    i = i + 1
    s = s + i
    print("i:",i)
    print("s:",s)
    if s > 5:
        break
    i = i + 1
    print("in( after breack ):", i)
print("out:", i)
