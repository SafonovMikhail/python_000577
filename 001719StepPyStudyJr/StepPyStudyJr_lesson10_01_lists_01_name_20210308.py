import random

# Initialization spaceship name
name = []
print('\n****************************************')
print('\tSPACESHIP ID-', end='')
for i in range(5):
    r = random.randint(0, 9)
    name.append(r)
    print(name[i], end='')
print('\n****************************************')
