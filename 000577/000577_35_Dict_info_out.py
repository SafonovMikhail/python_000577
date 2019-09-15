# 35 How to pick information out of a list of dictionaries
customer_29876 = {"first name": "David",
                  "last name": "Elliott",
                  "address": "4803 Wellesley St."
                  }
customer_first_name = customer_29876["first name"]
customers = [
    {
        "customer id": 0,
        "first name":"John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
        },
    {
        "customer id": 1,
        "first name":"Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
        },
    {
        "customer id": 2,
        "first name":"Jill",
        "last name": "Somers",
        "address": "3 Main St.",
        },
    ]
# How do we get any information out of them when we can't specify a dictionary name?
# In a list of strings, numbers, dictionaries, or anything else,
# the first item on the list gets an index of 0, provided automatically by Python
# Python assigns this dictionary the index 0
# очень важно, первому словарю присваивается номер ноль
# (!!!) нарисовать схему распределения ячеек памяти
# чтобы это смотрелось не просто рассказом.

# So all through the list of dictionaries, the customer id always matches the index of the dictionary.

# Let's say I want to know the address of a customer whose id is 2870. This is the code that finds it: 1 dictionary_to_look_in = customers[2870] 2 customer_address = dictionary_to_look_in["address"]

# The solution is to keep the original list of dictionaries intact,
# and create a second list of customers who are no longer active

# Then if, for example, you want to mail all active customers, you use the second list to filter inactive customers in the first list out of the mailing list.
