customer_29876 = {"first name": "David", "last name": "Elliott", "address": "4803 Wellesley St."}
# To the rescue comes looping.
cleanest_cities = ["Cheyenne", "cheyenne",
                   "Santa Fe", "santa fe", "Tucson", "tucson",
                   "Great Falls", "great falls",
                   "Honolulu", "honolulu"]
for a_clean_city in cleanest_cities:
    print(a_clean_city)
print("")
for each_value in customer_29876.values():
    print(each_value)
# Note: each_value is a variable.
# You can give it any legal variable name you like.
# Note:
# __dot__
# __values__
# __empty parentheses__
# __colon__
# Repeat:
# "Dot values parentheses colon."
# Вот так и нужно вдалбливать, автору респект, сильно экономит время
# в пособии так же стоит - по 10 раз повторять одно и то же, для того,
# чтобы, в конечном итоге, экономить время.
# что нужно делать - напечатать каждое значение: print each value
# (для каждого элемента в цикле)


