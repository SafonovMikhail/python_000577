for x in range(0, 3):
    print("We're on time %d" % (x))

# x = 1
# while True:
#     print("To infinity and beyond! We're getting close, on %d now!" % (x))
#     x += 1
print()
for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' % (x, y, x * y))

for x in range(3):
    print(x)
    if x == 1:
        break
print()
for x in range(3):
    print(x)
else:
    print('Final x = %d' % (x))
print()
string = "Hello World"
for x in string:
    print(x)
print()
collection = ['hey', 5, 'd']
for x in collection:
    print(x)
print()
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print(x)
print()


