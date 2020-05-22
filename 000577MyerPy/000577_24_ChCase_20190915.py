city_to_check = input("Enter your city: ")
city_to_check = city_to_check.lower()
print(city_to_check)
cleanest_cities = ["cheyenne", "santa fe", "tucson", "great falls", "honolulu"]
for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")
# Как вывести изначальный вариант, который вводил сам пользователь?
# Можно перевести в верхний регистр
city_to_check = city_to_check.upper()
print(city_to_check)
city_to_check = city_to_check.title()
print(city_to_check)



