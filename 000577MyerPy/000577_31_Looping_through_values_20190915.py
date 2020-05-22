# 000577_31_Looping_through_values
customer_29876 = {'first name': 'David', 'last name': 'Elliott', 'address': '4803 Wellesley St.', 'city': 'Toronto'}
print(customer_29876["first name"])
print(customer_29876["last name"])
print(customer_29876["address"])
# Recall  how  you  learned  to  loop  through  a  list
# Использовать цикл для выведения всех элементов по списку
print("\nИспользуем цикл для выведения всех элементов по списку: ")
for each_value in customer_29876.values():
    print(each_value)
'''
each_value - a variable to store the value for each iteration.
"Dot values parentheses colon." - DVPC

Exercise 1
Using a for loop, display each value in a dictionary.
Make up the variable names and the dictionary name.

Exercise 1 (answer)
for a_domain_name in websites.values(): # важно! Забыл про двоеточие, valueS вместо value
  print(a_domain_name)

----
Exercise 2
Complete this line:
for each_value in customer_29876.values_____ 

Exercise 2 (answer)
():
----
Exercise 3
In the orange box type the next character. 
I'll autocomplete. Don't type spaces or carriage returns.
To loop through the values in the products dictionary, complete this line:
for x in y_dictionary_________

Exercise 3 (answer)
.values():
----
Exercise 4
Code the first line to loop through the values in the y dictionary. 
The variable x holds each value.

Exercise 4 (answer)
for x in y.values():
----
Exercise 5
Code the first line that loops through the values of a dictionary. Make everything up.
  
Exercise 5 (answer)
for x in y.values():
----
Exercise 6
Looping through the values in a dictionary, display each value. Make everything up.

Exercise 6 (answer)
for an_animal in species.values():
  print(an_animal)
----
Exercise 7
Looping through the values in a dictionary, test 
if any of the values is less than 0. 
If so, display "ok" and break the loop.

y = {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1, 'zero': 0, 'neg 1': -1, 'neg 2': -2}
for x in y.values():
    if x < 0:
        print("ok")
        break
    else:
        print(x)
----
Exercise 8
Looping through the values in a dictionary, test if any of the values 
is equal to the modulo of 4 divided by 3. 
If so, display "ok" and break the loop.

Exercise 8(answer)
for x in y.values():
  if x == 4%3:
    print("ok")
    break
----
Exercise 9
Looping through the values in a dictionary, 
test if any of the values is equal to "arsenic". 
If so, append the value to the poisons list 
(use the variable from the loop, not the string, when appending) 
and break the loop.

Алгоритм выполнения:
1. Перебрать все значения в словаре
2. Сравнить значения с "arsenic"
3. append the value to the poisons list

stuff = {1:'qqq', 2:'www', 3:'arsenic', 4:'eee'}
poisons = []
print([poisons])
for item in stuff.values():
    if item == "arsenic":
        poisons.append("arsenic")
        break
print([poisons])
----




    
    


'''



