# 000562_04_ex02_vowels.py
# в развитие темы - написать программу, которая выводит количество гласных букв, в порядке возрастания частотности
vowels = set('aeiou') #
word = input ('Provide a word to search for vowels: ')
found = vowels.intersection(set(word))
for vowel in found:
	print (vowel)
input()