# 000562_04_ex03_def_vowels.py
# в развитие темы - написать программу, которая выводит количество гласных букв, в порядке возрастания частотности


def searsh4vowels(word:str)->set:#word - аргумент принимает строку(str), а возвращает множество (set())
	"""выводит гласные, находящиеся в веденном тексте"""
	vowels = set('aeiou') 
	found = vowels.intersection(set(word))
	for vowel in found:
		print (vowel)
#	return bool(found)

word = input ('Provide a word to search for vowels: ')
#print (searsh4vowels (word))
searsh4vowels (word)

input()