cities = ['Atlanta', 'Baltimore', 'Chicago', 'Denver', 'Los Angeles', 'Seattle']
# используем третий элемент списка
print("Welcome to " + cities[3])
print (cities)
cities = cities + ["Dubuque", "New Orleans"]
print (cities)
# добавляем элементы к существующему списку
longer_list_of_cities = cities + ["Dubuque", "New Orleans"]
print(longer_list_of_cities)
# создаем пустой список
todays_tasks = []
# который, впоследствии, заполняем значениями
todays_tasks = todays_tasks + ["Walk dog", "Buy groceries"]
print(todays_tasks)
# добавляем элемент в определенную позицию
cities.insert(0, "New York")
print(cities)
# добавляем элемента на место индекса 2 (остальные позиции смещаются)
cities.insert(2, "Dallas")
print(cities)
# новое значение для элемента
cities[2] = "Houston"
print(cities)
# Exercise 2
# Using the append keyword, add the number 1 to the end of the list nums.
print("ex02")
nums = [1,2,3]
nums.append(1)
print(nums)
# Exercise 3
# Using the keyword append, add the string "cat" to the end of the list pets.
print("ex03")
pets = [1,2]
pets.append('cat')
print(pets)
# Exercise 4
# Using the keyword append, add the string "sun" to the end of the list stars.
print("ex04")
stars = [1,2,3]
stars.append("sun")
print(stars)
# Exercise 5
# Code the alternative to the following statement, using the plus sign.
# x.append(5)
print("ex05")
x = []
x = x + [5]
print(x)
# Exercise 6
# Using the append keyword, append a string to a list. Make up the string and list name.
print("ex06")
x.append("miaou")
print(x)
# Exercise 7
# Using the plus sign instead of append, add two strings to the end of a list. Make up the list name and strings.
print("ex07")
x = x + ["tom", "netom"]
print(x)
# Exercise 8
# Insert the number 5 at the beginning of a list. Make up the list name.
print("ex08")
x.insert(0,5)
print(x)
# Exercise 9
# In the following list, insert a string after "orange". Make up the string.
# fruits = ["apple", "orange", "tangerine", "banana"]
print("ex09")
fruits = ["apple", "orange", "tangerine", "banana"]
fruits.insert(2, "nebanan")
print(fruits)
# Exercise 10
# Using the plus sign rather than append, add two numbers to the end of a list and assign the result to a second list. Make up the list names and the numbers.
print("ex10")
list1 = [1,2,3]
list2 = list1 + [4,5]
print(list2)
# Exercise 11
# Fill in the blank to assign the fifth element of the list to the variable.
# weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# fifth_weekday = weekdays[4]
# print(fifth_weekday)
print("ex11")
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekdays = weekdays + ["Sat"]
fifth_weekday = weekdays[4]
print(fifth_weekday)
print(weekdays)
# Exercise 12
# Create a list of three numbers. Then display the list.
print("ex12")
list = [1,2,3]
print(list)
