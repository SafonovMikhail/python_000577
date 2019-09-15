# 000577_09_ifStatements
'''
"if" (!)
Note that if is all lowercase. If you write
If instead of if: an error message.

"==" (!)
Whenever  you're  testing  whether  one  thing  is  the  same  as  another,  the
operator has to be ==.

indent(!)
'''
print("\npart 01:")
species = "cat"
if species == "cat":
    print("Yes, it's a cat!")

print("\npart 02:")
if species == "cat":
    status = "ok"
    kingdom = "animal"
    print(species, status, kingdom, "Yep, it's cat.", sep="___", end="~~~\n")

print("\npart 03: if returns bool: True or False (if 2+2 == 4:)")
if 2+2 == 4:
    status = "ok"
    kingdom = "animal"
    print(species, status, kingdom, "Yep, it's cat.", sep="___", end="~~~\n")

'''
Exercise 1
Rewrite this line so it's valid:
if species = "cat":
Solution: if species == "cat":

Exercise 2
Rewrite this line so it's valid:
if species == "cat"
Solution: if species == "cat":
! двоеточие

Exercise 3
Write the first line of an if statement that tests whether species is "cat"
Solution: if species == "cat":

Exercise 4
Code the first line of an if statement that tests 
whether x has the same value as y
Solution: if x == y:

Exercise 5
Code the first line of an if statement that tests 
whether one variable is the same as another. Make up the variable names.
Solution: if var1 == var2:

Exercise 6
Below, I've coded the first line of an if statement. 
Code the second line. The second line tells Python to display the string "OK". 
Don't forget to indent the second line.
if current_address == previous_address:
'''
print("\n000577_09_Ex06")
current_address = 1
previous_address = 1
if current_address == previous_address:
    print("OK")
'''
Exercise 7
On line 1, test whether a has the same value as b. 
On line 2, write that c equals d. Don't forget to indent the second line.

'''
print("\n000577_09_Ex07")
a = 1
b = 1
c = 2
d = 3

if a == b:
    # print("c == d")
    c = d
    print("c = ", c)
print("c = ", c)
'''
Exercise 8
If total has the value of 100, tax has the value of 2. Code both lines. 
'''
print("\n000577_09_Ex08")
total = 100
if total == 100:
    tax = 2
    print("outcome: ", total-(total*2/100))
'''
Exercise 9
If first_name is "Sherlock" last_name is "Holmes" and pal is "Watson". 
Code all three lines.
'''
print("\n000577_09_Ex09")
first_name = "Sherlok"
if first_name == "Sherlok":
    last_name = "Holmes"
    pal = "Watson"
print(first_name, last_name, pal, sep="___", end="~~~")
'''
Exercise 10
If you_won is "yes" tell Python to display "congrats". Code both lines.
'''
print("\n\n000577_09_Ex10")
you_won = "yes"
if you_won == "yes":
    print("congrats")
'''
Exercise 11
Correct the mistakes on line 2.
https://trinket.io/python3/c097da8c02
Solution: https://trinket.io/python3/770d38bf3d
'''
print("\n000577_09_Ex11")
species = "human"
if species == "human":
  print("correct")
'''
Exercise 12
Test if 2 equals 2. If it does, display ok
Solution: https://trinket.io/python3/e34c898e2e
'''
print("\n000577_09_Ex12")
if 2 == 2:
  print("ok")
