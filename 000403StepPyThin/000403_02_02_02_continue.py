i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    print("i:", i, " ", "s:", s)
    if s > 4:
        continue
    i = i + 1
    print("in (after continue): ", i)
print("i (out): ", i)