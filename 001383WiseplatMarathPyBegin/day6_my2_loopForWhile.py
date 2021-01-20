for i in range(5, 10):
    print(i)

array_a = ["one", "two", "three", "some", "any"]

for i in array_a:
    print(i)

array_b = [-4, 8, 9, -3, 0, 32, 100, 40, -20]
for i in array_b:
    if i > 0:
        print(i)

array_c = [5, 7, 2, 4, 0, -2, -4, -7]
for i in array_c:
    if i == 77:
        print("Нашли 77!")
        break
    print(i)
else:
    print("Не нашли 77 :(")

# while

ii = 0
while ii < 10:
    print(ii)
    ii += 1

# перечисление элементов массива
ii = 0
array_y = [1, 2, 3, 9, 8, 7, 0]
while ii < 7:
    print("array_y [", ii, "] ", ":", array_y[ii])
    ii += 1
