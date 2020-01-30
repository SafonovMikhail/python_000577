a = input()
b = input()
c = input()
d = input()

print("","\t",end="")
for i in range(int(c),int(d)+1):
    print(i, "\t", end="")
print()
for j in range(int(a), int(b)+1):
        print(j, "\t", end="")
        for i in range(int(c), int(d) + 1):
            print(i*j, "\t", end="")
        print()