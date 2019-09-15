# 000562_04_ex03_def_vowels.py
# в развитие темы - написать программу, которая выводит количество гласных букв, в порядке возрастания частотности


def searsh4vowels(word):
	"""выводит гласные, находящиеся в веденном тексте"""
	vowels = set('aeiou') 
	return vowels.intersection(set(word))

word = input ('Provide a word to search for vowels: ')
print (searsh4vowels (word))
#searsh4vowels (word)

input()