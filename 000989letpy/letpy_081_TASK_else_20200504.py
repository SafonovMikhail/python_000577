string = input()
# string = '#12345##6789'
# string = '# 123456789#'
# string =  '# 123456789#'
# string = '12345##6789'
# string = '12345#6789'
# string = '123456789'

# Измените программу из урока «Задача с выходом из цикла»
# так, чтобы при отсутствии двух решеток подряд она выводила
# в конце своей работы надпись «проверено»

i = 0
if string.find('##') == (-1):
    while True:
        # if string[i] != "#":
        print(string[i])
        i += 1
        if i == len(string):
            print('Проверено')
            break
else:
    i = 0
    while i < string.find('##'):
        # if string[i] != "#":
        print(string[i])
        i += 1
