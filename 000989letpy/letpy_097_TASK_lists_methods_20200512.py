list_ = input()
# list_ = "день победы 1945 года 9 мая"
list_01 = list_.split(' ')
num_ = []
for i in list_01:
    if i.isdigit(): # условие должно быть [True], можно не прописывать
        # print(list_01)
        num_.append(int(i))
# print(num_)
num_.sort() # не нужно создавать новый массив, преобразует (сказано было в теоретической части)
print(num_)
