# v01
print("Learn Python: action in progress...\n" * 3, end="")
print("Learn Python: action completed.\n" * 2)

# v02
a = 'Learn Python: action in progress...'
b = 'Learn Python: action completed.'
print(((a + '\n') * 3) + ((b + '\n') * 2))

# v03
l = "Learn Python: action in progress...\n" * 3
c = "Learn Python: action completed.\n" * 2
print(l + c)

# v04
a1 = "Learn Python:"  # интересная оптимизация кода!
a2 = " action in progress..."
a3 = " action completed."
print((a1 + a2 + "\n") * 3, end="")
print((a1 + a3 + "\n") * 2, end="")

# v05
[print(i) for i in
 ["Learn Python: action in progress...", "Learn Python: action in progress...", "Learn Python: action in progress...",
  "Learn Python: action completed.", "Learn Python: action completed."]]
# как оригинальный способ, после изучения циклов и списков (сгенерировать спискок)

# v06
x = "Learn Python: action in progress..."
y = "Learn Python: action completed."
[print(x) for f in range(3)]
[print(y) for f in range(2)]

# v07
for i in range(3): print('Learn Python: action in progress...')
for i in range(2): print('Learn Python: action completed.')

# v08
a = ['Learn Python: action in progress...', 'Learn Python: action completed.']
b = [3, 2]
for i in a:
    for j in range(b[a.index(i)]):
        print(i)
