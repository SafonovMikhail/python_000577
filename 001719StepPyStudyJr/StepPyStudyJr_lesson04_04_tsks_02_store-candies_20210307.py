# calculate
import math

price_1 = 270
price_2 = 200
gramm = int(input("Enter weight (gramm): "))
kg = gramm / 1000
print("Your weight: {} kg".format(kg))
if kg < 0.5:
    total = kg * price_1
else:
    total = kg * price_2
total = math.ceil(total) # магазин округляет до большего значения (?)
print("Your total: {} coin".format(total))
