# https://stepik.org/lesson/265081/step/12?discussion=1542627&thread=solutions&unit=246029
s, a, b, c = 0, int(input()), int(input()), int(input())
s += a if a > 0 else 0
s += b if b > 0 else 0
s += c if c > 0 else 0
print(s)
