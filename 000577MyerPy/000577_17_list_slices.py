# Exercise 1
# In the following code, smaller_list_of_cities is assigned __ elements of the cities list. (Enter a numeral.)
# smaller_list_of_cities = cities[2:5]
print("ex000577_17_01")
cities = [81, 36, 49, 25, 64, 9, 16, 1, 4]
smaller_list_of_cities = cities[2:5]
print(len(smaller_list_of_cities))

# Exercise 2
# Fill in the blank. The first element in the slice is the second element in the list.
# The last element in the slice is the third element in the list.
# smaller_list_of_cities = cities[____]
print("ex000577_17_02")
print(cities)
print(cities[1])
print(cities[3]) # index
print(cities[1:3]) # index (not includes in slice
# не обходимы еще задачи на эту тему

# Exercise 3
# In the orange box type the next character. I'll autocomplete. Don't type spaces or carriage returns.
# Copy the second through eighth elements from the list y and assign the slice to the list x.
print("")
print("ex000577_17_03")
y = [49, 144, 100, 64, 169, 121, 81, 4, 36, 9, 16, 196, 1, 25]
print(y)
leftlimit = 1 # int(input("left limit: "))
rightlimit = 9 # int(input("right limit: "))
print("[%s : %s]" %(leftlimit,rightlimit))
print("y[%s] = " %(rightlimit), int(y[rightlimit]))
x = y[leftlimit:rightlimit]
print(x)
print("initial lenth: ", len(y))
print("length of slice: ", len(x))

# Exercise 4
# Fail-safe coding. If you type the wrong character, I'll cancel the keystroke.
# Type spaces. When the exercise is complete, I'll turn the exercise number green.
# Reduce the list x to a slice of itself—the sixth through 8th elements.
print("")
print("ex000577_17_04")
print(y)
print("x[5:8]")
x1 = y[5:8]
print(x1)

# Exercise 5
# Copy some elements from a list and assign the slice to another list. Make up the list names and the index numbers.
# Press ctrl-Enter or click button to check answer.
print("")
print("ex000577_17_05")
# x1 = y[5:8]

# Exercise 6
# What is the index number of the last element in the slice?
# x = y[7:9]
print("")
print("ex000577_17_06")
print("8")

# Exercise 7
# Fill in the blank to slice the first through ninth element with minimal coding.
# x = y[____]
print("")
print("ex000577_17_07")
print("y = ", y)
x = y[:9]
print("x = y[:9]: ", x)
print("y[9] = ", y[9])

# Exercise 8
# Using minimal coding, copy the fifth through last element from y and assign the slice to x.
# Press ctrl-Enter or click button to check answer.
print("")
print("ex000577_17_08")
print("y = ", y)
x = y[5:]
print("x = y[5:]: ", x)
print("y[5] = ", y[5])
# предположительно неправильно, нужно с 4-го индекса делать, т.к. это пятый элемент

# Exercise 9
# Copy the numbers 2 through 4 out of y and assign the slice to x.
# y = [1, 2, 3, 4, 5]
print("")
print("ex000577_17_09")
y_ex000577_17_08 = [1, 2, 3, 4, 5]
print("y = ", y_ex000577_17_08)
x = y_ex000577_17_08[1:4]
print(x)


# Exercise 10
# Using minimal coding, reduce the list x to its first five elements.
print("")
print("ex000577_17_10")
print("y = ", y)
print(y[:5])

# Exercise 11
# Copy the middle two numbers out of list y and assign the slice to list x. Display list x.
print("")
print("ex000577_17_11")
y_ex000577_17_11 = [10, 11, 12, 13, 14, 15, 17, 18]
print("y = ", y_ex000577_17_11)
x_ex000577_17_11 = y_ex000577_17_11[3:5]
print(x_ex000577_17_11)

# Exercise 12
# Using minimal coding, reduce the list x to "elm" and "chestnut." Then display the list.
print("")
print("ex000577_17_12")
# print("y = ", y)
x_ex000577_17_12 = ["elm", "chestnut", "oak", "palm", "fir"]
x_ex000577_17_12 = x_ex000577_17_12[:2]
print(x_ex000577_17_12)
