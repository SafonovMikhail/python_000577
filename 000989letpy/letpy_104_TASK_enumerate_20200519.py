sentence = input()
sentence2 = sentence.split(' ')  # разделяем исходный текст
k = 0
l = 0
while k < len(sentence2):  # определяем количество элементов, без учета пробелов
    if sentence2[k] != '':  # можно бы усовершенствовать и искать небуквенные элементы
        l += 1
    k += 1
sentence3 = [0] * l
i = 0  # объявляем счетчик для перебора элементов списка [sentence2]
j = 0  # объявляем счетчик для элеметов списка [sentence3]
while i < len(sentence2):
    if sentence2[i] != '':
        sentence3[j] = sentence2[i]  # производим замену элементов массива [sentence3]
        j += 1
    i += 1
for i, e in enumerate(sentence3):
    # print(i, e)  # внимание, в примере нумерация слов начинается с 1, программа тест не прошла.
    print(i + 1, e)  # нумерация слов начинается с 1, программа тест прошла.
