# вариант нахождения вывода индекса при переборе коллекции
i = 0
list_ = ["Первое слово", "Второе", "Третье слово"]
for e in list_:
    print(i, e)
    i += 1

print() # просто для пробела

# более рациональный способ [enumerate]
list_ = ["Первое слово", "Второе", "Третье слово"]
for i, e in enumerate(list_):
    print(i, e)
