'''
Напишите программу, которая считывает строку, содержащую имя пользователя
и приветствует его, печатая строку вида "Привет, username", где вместо
"username" стоит введенное имя пользователя

Sample Input 1:

Кирилл
Sample Output 1:

Привет, Кирилл
Sample Input 2:

Alexandr
Sample Output 2:

Привет, Alexandr
'''
username = input()
print(f'Привет, {username}')
