vowels = ['a', 'e', 'i', 'o', 'u']
word = 'Milliways'
found = [] # объявляется пустой массив, в который будут складываться результаты поиска
for letter in word: # в каком слове ищем, перебираем каждый элемент [letter] списка [vowels]
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)
# [задание] вывести список гласных в слове на печать
print(found)
