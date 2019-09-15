# 000560_02_06_task01_while.py
i = 3
while i >= 0:
    print(i)
    i = i - 1
print('finished')

# 000560_02_06_ex02_endless.py
while 1 == 1:
    print('in the loop')

# 000560_02_06_task02_WhileDouble.py
x = 0
while x <= 20:
    print(x)
    x += 2

# 000560_02_06_ex03_break.py
i = 0
while 1 == 1:
    print(i)
    i = i + 1
    if i >= 5:
        print('breaking')
        break
print('Finished')

# 000560_02_06_task03_WhileBreak.py
i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break
print('Finished')

# 000560_02_06_ex04_continue.py
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

# 000560_02_06_LoopWhile.py
i = 1
while i <= 5:
    print(i)
    i = i + 1
print('finished')
