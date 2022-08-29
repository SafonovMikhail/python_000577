from tkinter import *

root = Tk()
root.title('test')
root.geometry('300x200+400+350')

# добавим кнопку
# btn = Button(root,text='Hello!',width=15,height=1,font=12)
# root - название главного окна
# ? позиционирование на экране

btn = Button(text='Hello!',
             background='blue',  # цвет ненажатой кнопки
             activebackground='yellow', # цвет нажатой кнопки
             foreground='white',  # цвет текста на ненажатой кнопке
             padx='50',  # ширина
             pady='2',  # вертикальные отступы
             font='12'
             )

btn.pack()  # ??

root.mainloop()
