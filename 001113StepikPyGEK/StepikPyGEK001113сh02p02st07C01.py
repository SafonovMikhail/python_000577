# Пример входных данных:
# material_1, size_1 = 1000, 2
# material_2, size_2 = 900, 2
# Пример выходных данных:
# Первое тело тяжелее на 2000 Н.

material_1, size_1 = 2700, 0.5
material_2, size_2 = 1200, 0.1
g = 10

f_1 = g * material_1 * size_1
f_2 = g * material_2 * size_2

print("Первое тело тяжелее на", f_1 - f_2, "Н.")
