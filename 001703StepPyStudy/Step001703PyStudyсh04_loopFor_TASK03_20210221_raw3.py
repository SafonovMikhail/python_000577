'''
Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B включительно, в порядке убывания. В этой задаче можно обойтись без инструкции if.
'''
a = int(input())
# a = 9
b = int(input())
# b = 0
if a % 2 == 0:
    for i in range(a - 1, b - 1, -2):
        print(i)
else:
    for i in range(a, b - 1, -2):
        print(i)

# v01
a = int(input())
# a = 9
b = int(input())
# b = 0
for i in range(a - (a + 1) % 2, b - 1, -2):
    print(i)
