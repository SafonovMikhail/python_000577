vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Введите предложение для поиска гласных (англ.): ')
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)
# [задание] вывести список гласных в слове на печать
print(found)
# [задание] дополнить программу так, чтобы провести частотный анализ текста [lorem ipsum]
