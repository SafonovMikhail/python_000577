print("000560_03_09_Test.py")

print()
print("q.01: min(a,b)")
def min(a,b):
    if a == b:
        return "even"
    elif a > b:
        return b
    else:
        return a
print(min(2,3))

print()
print("q.02: sum")

def sum(x):
    res = 0
    for i in range(0,x+1):
        res += i
    return res
print(sum(10))

print()
print("q.04: MaxNum")
def print_nums(x):
    for i in range(x):
        print(i)
    return
print_nums(10)

print()
print("q.05: OutPut")
def func1(x):
    res = 0
    for i in range(x):
        res += i
    return res
print(func1(4))