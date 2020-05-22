# theory

tasks = ["email Frank", "call Sarah", "meet with Zach"]
print(tasks)
print(tasks[0])# is "email Frank"
print(tasks[1])# is "call Sarah"
print(tasks[2])# is "meet with Zach"
'''
Working through the list from top to bottom, you complete "email Frank",
the first of the tasks. To strike that element off the list, you write:
'''
del tasks[0]
print(tasks)







print("")
print("000577_18_ex01")
tasks = ["email Frank", "call Sarah", "meet with Zach"]
tasks2 = tasks + [9,8,7,6,5,4,3,2,1,]
print(tasks)
print("del tasks[0]")
del tasks[0]
print(tasks)
tasks.remove("meet with Zach")
print("tasks.remove(\"meet with Zach\")")
print(tasks)

# Exercise 3
# Eliminate the element with an index of 2 from a list whose name is products.
print("")
print("000577_18_ex03")
products = tasks2
print("tasks2", tasks2)
del tasks2[3] # важно! индекс в квадратных скобках
print("del tasks2[3]: 9 ")
print("tasks2", tasks2)

# Exercise 4
# Eliminate "lamp" from the products list.\
print("")
print("000577_18_ex04")
print(products)
products.remove ("call Sarah") # важно! в круглых скобках
print(products)

# Exercise 5
# Eliminate "lamp" from the list using its index number.
# products = ["chair", "table", "lamp", "rug", "couch"]
print("")
print("000577_18_ex05")
products = ["chair", "table", "lamp", "rug", "couch"]
print(products)
del  products[2]
print(products)

# Exercise 6
# Eliminate "chair" from the list using its value.
# products = ["chair", "table", "lamp", "rug", "couch"]
print("")
print("000577_18_ex06")
products = ["chair", "table", "lamp", "rug", "couch"]
print(products)
products.remove("chair")
print(products)

# Exercise 7
# Eliminate an element from a list using its index number. Make up the list name and index number.
print("")
print("000577_18_ex06")
print(products)
del products[1]
print(products)

































