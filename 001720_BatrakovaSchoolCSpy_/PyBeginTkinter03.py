from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    root.title('Clicks {}'.format(clicks))


# счетчик кликов
root = Tk()
root.title('GUI на Python')
root.geometry('300x250')
btn = Button(text='Click me!',
             background='red',
             foreground='white',
             activebackground='yellow',
             padx='20',  # отступы по горизонтали
             pady='0',  # отсупы по вертикали
             font='16',
             command=click_button)
btn.pack()
root.mainloop()
