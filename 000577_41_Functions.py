# 41 Functions A function is a block of Python code that robotically
# does the same thing again and again, whenever you invoke its name

first_number = 2
second_number = 33
total = first_number + second_number


def add_numbers():
    first_number = 2
    second_number = 3
    total_01 = first_number + second_number
    print(total_01)
# вызов функции
# add_numbers()

def add_numbers(a,b):
    first_number = a
    second_number = b
    total = first_number + second_number
    print(total)
    return total
# вызов функции
add_numbers(10,20)
print("total: ", total)
print(type(total))
# Неумничать, а задать вопрос на форумах, автору
# автору предложить сделать андроид программу по курсу
# премиум подписка открывает доступ к многочисленным упражнениям (по умлочанию, упражнений не более 3-х
