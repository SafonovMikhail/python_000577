msg = "Hello World!"
# одна и та же строка! Не копия
copy = msg[:]
print(id(copy), id(msg))

myStr = msg[:6]+"w"+msg[7:9]+msg[10:]
print(myStr)
