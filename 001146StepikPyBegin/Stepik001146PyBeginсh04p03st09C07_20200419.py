# p1 = [int(input()), int(input())]
# p2 = [int(input()), int(input())]

# p1 = [1, 3]
# p2 = [4, 8]

# p1 = [2, 4]
# p2 = [4, 8]

# p1 = [3, 5]
# p2 = [4, 8]

# p1 = [4, 6]
# p2 = [4, 8]

# p1 = [5, 7]
# p2 = [4, 8]

# p1 = [6, 8]
# p2 = [4, 8]

# p1 = [7, 9]
# p2 = [4, 8]

# p1 = [8, 10]
# p2 = [4, 8]

# p1 = [9, 11]
# p2 = [4, 8]

# p1 = [4, 8]
# p2 = [4, 8]

p1 = [-8, -4]
p2 = [-5, -3]

if abs(p1[1] - p1[0]) > abs(p2[1] - p2[0]):
    p1, p2 = p2, p1
if p2[0] > p1[1] or p1[0] > p2[1]:
    print("пустое множество")
# отрезки равны
elif p1[0] == p2[0] and p1[1] == p2[1]:
    print(p1[0], p1[1])

elif p1[1] < p2[1] and p1[0] < p2[0]:
    print(p2[0], p1[1])
elif p1[1] == p2[0]:
    print(p1[1])
elif p1[0] == p2[1]:
    print(p1[0])
elif (p1[1] > p2[1]):
    print(p2[1], p1[1])
elif (p1[0] > p2[0]) or (p1[0] == p2[0]):
    print(p1[0], p1[1])
elif (p2[1] > p1[1]) or (p2[1] == p1[1]):
    print(p2[0], p1[1])
elif (p1[1] == p2[0]):
    print(p1[1])
elif (p1[0] == p2[1]):
    print(p1[0])
