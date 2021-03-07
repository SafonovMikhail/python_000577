# random numbers
import random

number = 0
num_check = 250000
for i in range(num_check):
    # random number from 1 to 6
    magic_number = random.randint(1, 6)  # границы входят в диапазон.
    # print("{}. The magic number is: {} ".format(i, magic_number))
    if magic_number == 6:
        number = number + 1
print("You got number 6: {} times".format(number))
prob = number / num_check * 100
print(f'вероятность - {prob} %')
print(100 / prob)
