import random
num = int(input("Введите число элементов в списке: "))
a = [ i*i for i in range(1,num+1)]
random.shuffle(a)
print("")
print(a)

# Чтобы вывести уникальные слова из списка в случайном порядке,
# используя различные генераторы псевдослучайных чисел:
# import random
print("")
words =  ["Alex", "Kate", "Love", "World", "Peace", "Putin",]
unique_words = list(set(words))
random.shuffle(unique_words) # shuffle using default Mersenne Twister generator
print("\n".join(unique_words))
print(words)
print('')
random.SystemRandom().shuffle(unique_words)  # OS-provided generator
print("\n".join(unique_words))
print(words)


# def display():
#     s1 = []
#     for i in range(9): # This is just to tell you how to create a list.
#         s1.append(i)
#         return s1
# display()
# print display()
