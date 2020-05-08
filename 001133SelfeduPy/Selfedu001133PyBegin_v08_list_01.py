lst = ["Москва", "Санкт-Петербург", "Тверь", "Казань"]
print(type(lst))
print(lst)
print(lst[0])

# for i in (len(lst) - 1):
for i in range(len(lst)):
    print(lst[i])

# for i in lst:
#     print(lst)

digs = [-1, 0, 5, 3, 2]
print(digs)
# замена значений списков на соответствующие квадраты
for x in range(5):
    digs[x] **= 2  # digs[x] = digs[x]**2
print(digs)

print("# создать список заданной размерностью: ")
list1000 = [0] * 100
print(list1000)
for i in range(len(list1000)):
    print(list1000[i], sep="$",end="") # почему [sep] не работает?
    # print("выводим на печать")
