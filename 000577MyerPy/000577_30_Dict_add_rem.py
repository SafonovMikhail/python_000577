# 000577_30_Dict_add_rem
customer_29876 = {'first name': 'David', 'last name': 'Elliott', 'address': '4803 Wellesley St.', 'city': 'Toronto'}
print("initial dict", customer_29876)
# rem
del customer_29876["address"]
print('remove "address"',customer_29876)
# add "street"
print("add street")
customer_29876["street"] = "Park Avenue"
print(customer_29876)
# change "Winipeg"
print('change city from Toronto to Winipeg')
customer_29876["city"] = "Winipeg"
print(customer_29876)