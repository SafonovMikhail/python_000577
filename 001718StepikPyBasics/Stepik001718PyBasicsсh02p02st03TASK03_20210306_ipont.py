'''
Миша давно копил деньги на новую модель телефона IPont 13 и чехол для него. Напишите программу, которая поможет Мише определить, достаточно ли у него финансов для покупки обоих предметов

Формат входных данных

На первой строчке вводится целое число – Мишины накопления, на второй – стоимость телефона, на третьей – стоимость чехла для телефона

Формат выходных данных

“Да”, если денег достаточно, “Нет” в остальных случаях.

Sample Input 1:

70000
55000
1500
Sample Output 1:

Да
Sample Input 2:

30000
45000
1000
Sample Output 2:

Нет
'''
n1_skopil = int(input())
n2_tel = int(input())
n3_chehol = int(input())
if n1_skopil < n2_tel + n3_chehol:
    print('Нет')
else:
    print('Да')
