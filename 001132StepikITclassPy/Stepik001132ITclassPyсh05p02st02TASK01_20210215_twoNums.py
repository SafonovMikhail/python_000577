'''
Напиши программу, которая без использования функций max и min, находит наибольшее и наименьшее из двух чисел.

Sample Input 1:

1
5
Sample Output 1:

Наибольшее число 5
Наименьшее число 1
Sample Input 2:

0
0
Sample Output 2:

Наибольшее число 0
Наименьшее число 0
'''
n1 = int(input())
n2 = int(input())
if n1 > n2:
    print(f"Наибольшее число {n1}")
    print(f"Наименьшее число {n2}")
else:
    print(f"Наибольшее число {n2}")
    print(f"Наименьшее число {n1}")