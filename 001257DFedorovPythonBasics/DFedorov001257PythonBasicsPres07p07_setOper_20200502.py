s1 = set(range(5))
s2 = set(range(2))
print(s1, s2)
s1.add(5)
print(s1)
print(s1.intersection(s2))  # пересечение множеств
print(s1 & s2)  # другое обозначение пересечения множеств
s3 = set(range(10))
print("s3: ", s3)
print(s1.union(s3)) # объединение множеств
# https://docs.python.org/3/tutorial/datastructures.html#sets подробнее

