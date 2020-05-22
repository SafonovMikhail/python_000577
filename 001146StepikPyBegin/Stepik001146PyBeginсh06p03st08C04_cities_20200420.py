input1 = (input(), input(), input())
# input1 = ("Марсель", "Париж", "Лион")
minlen = input1[0]
maxlen = input1[0]
if len(minlen) > len(input1[1]):
    minlen = input1[1]
if len(minlen) > len(input1[2]):
    minlen = input1[2]
if len(maxlen) < len(input1[1]):
    maxlen = input1[1]
if len(maxlen) < len(input1[2]):
    maxlen = input1[2]
print(minlen)
print(maxlen)
