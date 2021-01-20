f = '10'
if f == str(10):
    print("f==10")
h = 10
if h == int('10'):
    print("h=='10'")
j = "2.53"
print(float(j) + 7.5)

age = int(input("Введите Ваш возраст: "))

if age == 5:
    print("5!")
elif age == 6:
    print("6!")
elif age == 7:
    print("7!")

if age < 100:
    print("age<100")
else:
    print("Вам больше или равно 100")

if age > 20:
    print("О, вы так стары?!")
    print("Вам больше, чем 20?")

if age < 10:
    print("О, Вам так мало лет?")

if age == 18:
    print("Ура, мне 18, еду, куда хочу!")

if age >= 30 and age <= 40:
    print("Ооо, от 30 до 40!")

if age == 50 or age == 60 or age == 70 or age == 80:
    print("О, у Вас юбилей")

print("Мы проверили Ваш возраст")
