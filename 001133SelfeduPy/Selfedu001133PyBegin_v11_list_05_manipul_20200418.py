import random

print("ListGen[n1]:")
n1 = 30
list1 = list(range(n1))
print(list1)

print()
print("ListGen[n2]:")
n2 = 30
list2 = [random.randint(0, 999) for i in range(n2)]
print(list2)
print("list2_01[<400]:")
list2_01 = [num for num in list2 if num < 400]
print(list2_01)

print()
print("ListGen[n4](evenNums):")
n4 = 30
list4 = [random.randint(0, 999) for i in range(n4) if i % 2 == 0]
print(list4)

print()
print("ListGen[n3]:")
n3 = 11
A = list(range(n3))
print(A)
print("ListGen[n3] (reverse):")
for i in range(n3 // 2):
    A[i], A[n3 - i - 1] = A[n3 - i - 1], A[i]
print(A)

print()
print("List[A](len=8):")
A = [2, 2, -1, -5, 55, 34, 0, 10]
print(A)
N = len(A)
for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
print("List[A](len=8, ordered):")
print(A)
