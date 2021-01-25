count = 0
for a in range(1, 150):
    for b in range(1, 150):
        for c in range(1, 150):
            for d in range(1, 150):
                for e in range(1, 150):
                    print(f"a:{a}, b:{b}, c:{c}, d:{d}, e:{e}")
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(f"a:{a}, b:{b}, c:{c}, d:{d}, e:{e}")
                count += 1
print(count)
'''
не запускать! зависнет. для начала упроситть, сократить
'''
