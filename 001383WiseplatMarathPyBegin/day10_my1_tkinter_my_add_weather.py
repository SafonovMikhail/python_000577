from tkinter import *
import requests

# импортируем библиотеку requests
root = Tk()


# https://openweathermap.org/current
# KEY=
# URL=http://api.openweathermap.org/data/2.5/weather


def get_weather():
    # получаем данные от пользователя
    city = cityField.get()
    key = 'f940e13d1c93f0a48440f7eba57c463b'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    # параметры прописываем в отдельный [словарь]
    # Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    print(city)
    result = requests.get(url, params=params)
    # Получаем JSON ответ по этому URL
    weather = result.json() # нужно знать, что такое JSON


    # print(weather) #получим весь ответ в командной строке
    # Москва
    # {'coord': {'lon': 37.62, 'lat': 55.75}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 66.34, 'feels_like': 65.01, 'temp_min': 64.4, 'temp_max': 68, 'pressure': 1011, 'humidity': 93}, 'visibility': 10000, 'wind': {'speed': 11.18, 'deg': 280}, 'clouds': {'all': 75}, 'dt': 1596085323, 'sys': {'type': 1, 'id': 9029, 'country': 'RU', 'sunrise': 1596072690, 'sunset': 1596130813}, 'timezone': 10800, 'id': 524901, 'name': 'Moscow', 'cod': 200}
    # Seattle
    # {'coord': {'lon': -122.33, 'lat': 47.61}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 69.13, 'feels_like': 66.67, 'temp_min': 63, 'temp_max': 75.2, 'pressure': 1014, 'humidity': 46}, 'visibility': 10000, 'wind': {'speed': 3.36, 'deg': 0}, 'clouds': {'all': 1}, 'dt': 1596085326, 'sys': {'type': 1, 'id': 3417, 'country': 'US', 'sunrise': 1596026624, 'sunset': 1596080856}, 'timezone': -25200, 'id': 5809844, 'name': 'Seattle', 'cod': 200}

    # записываем ответ в отдельную переменную
    # Полученные данные добавляем в текстовую надпись для отображения пользователю
    info['text'] = f'{str(weather["name"])}:{weather["main"]["temp"]}' # разбирать синтаксис

# настройки главного окна
root['bg'] = '#fafafa' # фоновый цвет
root.title("Погодное приложение") # название окна
root.geometry('300x250') # размеры окна
root.resizable(width=False, height=False) # запрет на изменение размеров окна
# Создаем фрейм (область для размещения других объектов)
frame_top = Frame(root, bg='#ffb700', bd=5) # Указываем к какому окну он принадлежит, какой у него фон и какая обводка

# Также указываем его расположение
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

# Создаем второй фрейм (область для размещения других объектов)
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

# Создаем текстовое поле для получения данных от пользователя
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack() # размещаем объект

# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()


info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()
