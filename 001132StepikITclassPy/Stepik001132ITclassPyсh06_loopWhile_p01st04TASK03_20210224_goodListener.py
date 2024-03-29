'''
Программа "Хороший слушатель". Пользователь рассказывает программе все, что хочет печатая строки текста. Программа ничего не отвечает, и "слушает". И только когда пользователь в одной из строк введет слово "спасибо", то программа выводит сообщение:

Вы сегодня хорошо выговорились и для этого Вы напечатали n знака(ов).
Где вместо n - программа должна вывести кол-во символов текста, набранных пользователем.

Sample Input:

Привет. Мои дела хорошо.
Но бывает не очень
как сделать чтобы было всегда хорошо?
Ладно спасибо
Sample Output:

Вы сегодня хорошо выговорились и для этого Вы напечатали 92 знака(ов).
'''
s = input()
lens = 0
while True:
    if 'спасибо' not in s:
        lens += len(s)
        s = input()
    else:
        lens += len(s)
        print(f'Вы сегодня хорошо выговорились и для этого Вы напечатали {lens} знака(ов).')
        break