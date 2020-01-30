y = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(y)
x = y[:9]
print("x = y[:9]")
print(x)
print(("element %s" %y[9])+("(index %s)")%y.index(6) + ", not in slice")
print("so, if I want first nine elements, I must write: x2 = y[:10]")
x2 = y[:10]
print(x2)
print(("element %s" %y[9])+("(index %s)")%y.index(6) + ", in slice")