# 000577_30_Dict_add_rem
customer_29876 = {'first name': 'David', 'last name': 'Elliott', 'address': '4803 Wellesley St.', 'city': 'Toronto'}
# rem
del customer_29876["address"]
print(customer_29876)
# add
customer_29876["street"] = "Park Avenue"
# change
customer_29876["city"] = "Winipeg"
print(customer_29876)