fio = ('Иванов Иван Иванович'.split())
print(fio)
print(type(fio))

# преобразовать в список, возможно наличие пробелов.
digs = "1, 2,3, 4,5,6"
digs = digs.replace(" ", "").split(",")
print(digs)
