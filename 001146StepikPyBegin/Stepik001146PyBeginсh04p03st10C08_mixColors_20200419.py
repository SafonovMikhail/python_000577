c = sorted([input(), input()])
if (c[0] == "желтый" and c[1] == "красный"):
    print("оранжевый")
elif (c[0] == "красный" and c[1] == "синий"):
    print("фиолетовый")
elif (c[0] == "желтый" and c[1] == "синий"):
    print("зеленый")
else:
    print("ошибка цвета")