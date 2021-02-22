'''
Задача «Второе вхождение»
Условие
Дана строка. Найдите в этой строке второе вхождение буквы f, и выведите индекс этого вхождения. Если буква f в данной строке встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
'''
s = input()
# s = 'coffee'
# s = 'ffffffffffffffff'
# s = 'foooooooooooooof'
if s.find('f') == -1:
    print(-2)
elif s.find('f') == s.rfind('f'):
    print(-1)
else:
    left_bord = s.find('f') + 1
    # print(type(left_bord))
    print(s[left_bord:].find('f') + left_bord)
