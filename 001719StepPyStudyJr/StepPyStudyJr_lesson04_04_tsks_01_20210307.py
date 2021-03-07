'''
перевод из миль в километры
'''
# miles to km
n = input("Enter miles: ")
mile = 1.609
km = float(n) * mile
print(f"{n} mile = {km} km")
if km > 80:
    print("Too fast!")
