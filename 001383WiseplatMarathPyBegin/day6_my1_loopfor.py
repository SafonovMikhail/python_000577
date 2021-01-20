# цикл for
for i in range(0, 5):
    print("привет %s" % i)
    print("Ура!")

print(list(range(10, 17)))

sp1 = [10, 40, 50, 77, 99, 101, 230]
sp2 = ["привет", "мир", "ура", "победа", "да", "нет"]

for i in sp1:
    print(i)
    for j in sp2:
        print(j)

for i in range(0, 5):
    for j in range(0, 5):
        print("%s_%s" % (i, j))

found_coins = 20
magic_coins = 10
stolen_coins = 2
coins = found_coins
print(found_coins + 365 * (magic_coins - stolen_coins))

# для просмотра промежуточных значений будем использовать цикл.
for i in range(0, 365):
    coins = coins + magic_coins - stolen_coins
    print("День %s стало монет %s" % (i, coins))
