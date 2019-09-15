print("000560_02_06_ex01_loop:while")
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Finished!")

print("")
print("000560_02_06_task01_loop:while")
i = 3
while i >= 0:
    print(i)
    i = i - 1
print('finished')

print("")
print("000560_02_06_ex02_endless")
# while 1 == 1:
# print('in the loop')

print("")
print("000560_02_06_task02_WhileEven")
x = 0
while x <= 20:
    print(x)
    x += 2

print("")
print("000560_02_06_ex03_break")
i = 0
while 1 == 1:
    print(i)
    i = i + 2
    if i >= 10:
        print("if i >= 10:")
        print('breaking')
        break
print('Finished')

print("")
print("000560_02_06_task03_WhileBreak")
i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        print("break")
        break
print('Finished')

print("")
print("000560_02_06_ex04_continue")
i = 0
while True:
    i = i + 1
    if i == 2:
        print('skipping(i=2)')
        continue
    if i == 5:
        print('breaking(i=5)')
        break
    print(i)

print('Finished')

print("")
print("000560_02_06_LoopWhile")
i = 1
while i <= 5:
    print(i)
    i = i + 1
print('finished')
