# import tkinter
from tkinter import *

root = Tk()


# [09] создаем функцию для нажатия на кнопку
def btn_click():
    login = loginInput.get()
    password = passField.get()
# [11]
    info_str = f'Данные: {str(login)}, {str(password)}'
# [10] создаем всплывающее окно с выводом введенных значений
    messagebox.showinfo(title='Название', message=info_str)
# [12] окно с ошибкой
    messagebox.showerror(title='', message='Error always!')

root['bg'] = '#fafafa'
root.title('Полупрозрачное окно')
root.geometry('300x250')
root.resizable(width=False, height=False)
root.wm_attributes('-alpha', 0.7)

# [02] создаем рабочее пространство (на его фоне можем рисовать объекты)
canvas = Canvas(root, height=300, width=250)
canvas.pack()  # проявляем его

# [03] рамка для создания ругих визуальных компонентов
frame = Frame(root, bg='red')  # root - указание, какому окну он принадлежит
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

# [04] создание текстовой надписи
title = Label(frame, text='Текст подсказка', bg='gray', font=40)
title.pack()

# [05] создание кнопки
# [08] добавляем отслеживание нажатия на кнопку [command=]
btn = Button(frame, text='Кнопка', bg='yellow', command=btn_click)
btn.pack()

# [06] создание текстового поля
loginInput = Entry(frame, bg='white')
loginInput.pack()

# [07] создание поля "пароль"
passField = Entry(frame, bg='white', show='*')  # [show] - какие символы будут показываться вместо вводимых
passField.pack()

root.mainloop()
