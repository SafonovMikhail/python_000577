# You can copy consecutive elements of a list to build another list.
# For example, if you have this list…
print("p01")
cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]
print(cities)
# …you can copy elements 2 through 4 to create another list…
print("p02")
smaller_list_of_cities = cities[2:5]
print(cities)
print(smaller_list_of_cities)
# When the first element of the slice is the first element of the original list the element with
# an index of 0—you can omit the first number altogether:
# smaller_list_of_cities = cities[:5]
print("p03")
print(smaller_list_of_cities)
print(smaller_list_of_cities[:2])
# When the last element of the slice is the last element of the original list, you
# can omit the second number:
# smaller_list_of_cities = cities[2:]
print("p04")
smaller_list_of_cities = smaller_list_of_cities + ["Atlanta", "Dallas"]
print(smaller_list_of_cities)
print(smaller_list_of_cities[3:])
# пока не вижу, как вывести индекс
# Exercise 1
# In the following code, smaller_list_of_cities is assigned __ elements of the cities list. (Enter a numeral.)
# smaller_list_of_cities = cities[2:5]
print("ex01")
print(cities)
print("list legth %s" %len(cities))
smaller_list_of_cities = cities[2:5]
print("smaller_list_of_cities = cities[2:5]")
print(smaller_list_of_cities)
print("index of 'LA': %s" %cities.index("Los Angeles"))
# Exercise 2
# Fill in the blank. The first element in the slice is the second element in the list.
# The last element in the slice is the third element in the list.
# smaller_list_of_cities = cities[____]
print("ex02")
smaller_list_of_cities = cities[1:3]
print(cities)
print("smaller_list_of_cities = cities[1:3]")
print(smaller_list_of_cities)
# Exercise 3
# In the orange box type the next character. I'll autocomplete. Don't type spaces or carriage returns.
# Copy the second through eighth elements from the list y and assign the slice to the list x.
print("ex03")
y = [1,2,3,4,5,6,7,8,9,10]
x = y[1:8]
print(y)
print(x)
# Exercise 4
# Fail-safe coding. If you type the wrong character, I'll cancel the keystroke.
# Type spaces. When the exercise is complete, I'll turn the exercise number green.
# Reduce the list x to a slice of itself—the sixth through 8th elements.
print("ex04")
x = y
print(x)
x = x[5:8]
print(x)
# Exercise 5
# Copy some elements from a list and assign the slice to another list. Make up the list names and the index numbers.
print("ex05")
print(y)
x = y[1:5] # это индексы. Первый входит, последний не входит
print(x)
# Exercise 6
# What is the index number of the last element in the slice?
# x = y[7:9]
print("ex06")
print(y) # 10 элементов
print("длинна массива %s" %len(y))
x = y[7:9] # из 10 элементов (индексы 0-9), выбирается с элемента с индексом 7 [8] по элемент с индексом 9 [10]
print("x = y[7:9]")
print(x)
# Exercise 7
# Fill in the blank to slice the first through ninth element with minimal coding.
# x = y[____]
print("ex07")
y2 = y + [11,12,13,14,15]
y2.reverse() # просто разворачивает массив без присвоения его новому.
print("длинна массива %s" %len(y2))
print(y2)
print("x = y3[:9]")
print(("элемент %s" %y2[9])+("(индекс %s - десятый элемент списка!)")%y2.index(6) + ", в промежуток не входит")
x = y2[:9] #(выводит элемент с индексом 8, значит, 9 - граничное значение, не включено)
print(x)
print("длинна списка %s" %len(x))
print("индекс элемента 7: %s" %y2.index(7))
print("десятый элемент %s" %y2[9])


