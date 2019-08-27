cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
city_to_check = input("city_to_check: ")
for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")
        break

