foo = "Привет, мир!"
print(foo[8:11]) # >>> мир: [8:11)
print(foo[-10:-6]) # >>> ивет: [-10:-6)
print(foo[:6])
print(foo[-4:])
print(foo[:100]) # неуществующие индексы не вызывают ошибки (будет выведена вся строка)
print(foo[200:300]) # не будет выведено ничего


