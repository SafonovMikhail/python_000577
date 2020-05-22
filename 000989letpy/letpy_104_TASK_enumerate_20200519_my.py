# sentence = input()
sentence = 'Привет миру мир  труд    май'
# sentence1 = sentence.replace('  ', ' ')
print("sentence:", sentence)
sentence2 = sentence.split(' ')  # разделяем исходный текст
print("sentence2:", sentence2)  # печатаем получившийся список
k = 0
l = 0
while k < len(sentence2):  # определяем количество элементов, без учета пробелов
    if sentence2[k] != '':  # можно бы усовершенствовать и искать небуквенные элементы
        l += 1
    k += 1

print()

sentence3 = [0] * l
print("sentence3:", sentence3)
# sentence3 = [] - не получится просто объявить пустой список. Необходимо задать количество элементов
# обязательно вопрос в stackoverlow, почему не работает append

i = 0 # объявляем счетчик для перебора элементов списка [sentence2]
j = 0 # объявляем счетчик для элеметов списка [sentence3]

print()

print("len(sentence2):", len(sentence2))
print("len(sentence3):", len(sentence3))

while i < len(sentence2):
    if sentence2[i] != '':
        sentence3[j] = sentence2[i]
        j += 1
        # print("sentence3", sentence3)
    i += 1
print("sentence3:", sentence3)

print()

for i, e in enumerate(sentence2):
    print(i, e)

print()

for i, e in enumerate(sentence3):
    print(i, e)
