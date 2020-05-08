for x in 1, 5, 2, 4:
    print(x ** 2)

print()
print("# используем генератор последовательностей")
for x in range(1, 5, 1):
    print(x)

print("# (1,5,-1): генерирует пустую последовательность):   ")
for x in range(1, 5, -1):
    print(x)

print()
print("# (5,0,-1): правильно сгенерированная последовательность):   ")
for x in range(5,0,-1):
    print(x)



    
