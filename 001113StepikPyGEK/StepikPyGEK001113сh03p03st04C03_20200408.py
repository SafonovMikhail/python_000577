s = float(input())
sut = s // (24 * 3600)
h = (s % (24 * 3600)) // 3600
m = ((s % (24 * 3600)) % 3600) // 60
print(h, m)
