# ----------------------------
print('# Слияние двух отсортированных списков')


def merge(list1, list2):
    result = list1 + list2  # создаем результирующий список
    result.sort()  # сортируем список встроенным методом sort()
    return result  # возвращаем отсортированный список


list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = merge(list1, list2)  # вызываем функцию слияния двух отсортированных списков
print(list3)
print()

# ----------------------------
print('# Быстрое слияние двух отсортированных списков в один')


def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list1, list2)
print(list3)
print()

# ----------------------------
print('# Измерение времени выполнения сортировки')
import timeit
import random


# merge sort using default library 
def merge(list1, list2):
    return sorted(list1 + list2)


# from stepic
def quick_merge(list1, list2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    return result


numbers1 = sorted([random.randint(1, 2000000) for _ in range(1000000)])
numbers2 = sorted([random.randint(1, 2000000) for _ in range(2000000)])

start = timeit.default_timer()
merge(numbers1, numbers2)
print("Processing time merge: %s" % (timeit.default_timer() - start))

start = timeit.default_timer()
quick_merge(numbers1, numbers2)
print("Processing time quick_merge: %s" % (timeit.default_timer() - start))
print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')

print()

# ----------------------------
print('# ')
