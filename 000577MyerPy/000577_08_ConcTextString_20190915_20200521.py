# http://www.asmarterwaytolearn.com/python/index-of-exercises.html
from xxsubtype import spamdict

# from macholib.mach_o import fat_arch

print("HW!")
greeting = "HW!"
print(greeting)

greeting = "H"
addressee = "W"
whole_greeting = greeting + addressee
print(whole_greeting)

'''
Exercise 1
To combine two strings, you __________ them.
Answer: concatenate

Exercise 2
Strings have been assigned to the variables a and b. 
Concatenate them and assign the result to the variable c.
Answer: c = a + b

Exercise 3
Concatenate "Mr. " and "Brown". Assign the result to the variable person.
Answer: person = "Mr. " + "Brown"

Exercise 5
Concatenate "Hello, " and "world!". Assign the result to a variable. 
Make up the variable name. Don't forget the space at the end of the first string.
'''
print("000577_08_Ex05")
greeting = "Hello " + "world!"
print(greeting)
greeting = "Hello", "world!"
print(greeting,end="\n\n")

'''
Exercise 6
Concatenate three variables. Assign the result to a fourth variable. 
Make up the variable names.
'''
print("000577_08_Ex06")
var2 = "H"
var3 = "W"
var4 = "!"
var1 = var2 + var3 + var4
print(var1,end="\n\n")
'''
Exercise 7
Concatenate three strings: your first name, a space, and your last name. 
Assign the result to a variable. Make up the variable name.
'''
print("000577_08_Ex07")
firstName = "Mikhail"
lastName = "Safonov"
space = " "
fullName = firstName+space+lastName
print(fullName,end="\n\n")
'''
Exercise 8
Give yourself a fancy title, like Sir Mark or Lady Judith. 
Concatenate the title plus a space plus your first name. 
Assign the result to a variable. Make up the variable name.
'''
print("000577_08_Ex08")
title = "Sir"
firstName = "Mikhail"
print(title+" "+firstName, end="\n\n")
'''
Exercise 9
Give yourself a fancy title. But this time 
1. include the space in the first string. 
So you'll be concatenating the title and space as the first string, 
and your first name as the second string. Assign the result to a variable. 
Make up the variable name.
'''
print("000577_08_Ex09")
title = "Sir "
firstName = "Mikhail"
print(title+firstName, end="\n\n")
'''
Exercise 10
In a single statement, tell Python to display the concatenation of two variables. 
'''
print("000577_08_Ex10")
title = "Sir "
firstName = "Mikhail"
print(title+firstName, end="\n\n")
'''
Exercise 11
https://trinket.io/python3/cb7babb4b1
On line 3 code a single line, using the two variables 
plus a string between them, that displays Hello, World!
Solution: https://trinket.io/python3/ff88b2df9d
'''
print("000577_08_Ex11")
first_word = "Hello"
second_word = "World!"
comma = ", "
print(first_word+comma+second_word, end="\n\n")
'''
Exercise 12
Assign three strings to three different variables. 
Concatenate them and assign the result to a fourth variable. 
Display the concatenated string using the fourth variable.
Solution: https://trinket.io/python3/521e64579c
'''
print("000577_08_Ex12")
var1='var1 '
var2='var2 '
var3='var3 '
var4=var1+var2+var3
print(var4,end="\n\n")
