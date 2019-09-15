# 000560_03_06_task01_functions_var.py
# переменной можно назначить функцию

def shout(word):
	return word + '!'
speak=shout
output=speak("shout")
print (output)