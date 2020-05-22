# 000562_04_ex03_def_vowels.py
# в развитие темы - написать программу, которая выводит количество гласных букв, в порядке возрастания частотности


def searsh4vowels(phrase:str)->set:#phrase - аргумент принимает строку(str), а возвращает множество (set())
	"""выводит гласные, находящиеся в веденном тексте"""
	vowels = set('aeiou') 
	found = vowels.intersection(set(phrase))
	for vowel in found:
		print (vowel)
#	return bool(found)
#searsh4vowels (phrase)

def search4letters(phrase:str,letters:str='aeiou')->set:
	"""возвращает множество букв из 'letters', найденных в указанной фразе"""
	return set(letters).intersection(set(phrase))

phrase = input ('phrase: ')
letters = input ('letters: ')
#print (searsh4vowels (phrase))
print (search4letters (phrase, letters))

input()