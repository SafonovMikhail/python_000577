numGoodRep = int(input())
city = input()
lang = input()
if numGoodRep >= 7 and city == "Рим" and ("английский" in lang or "русский"in lang):
    print("Подходит")
else:
    print("Не подходит")
