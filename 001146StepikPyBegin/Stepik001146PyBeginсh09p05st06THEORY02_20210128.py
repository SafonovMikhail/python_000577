age = 27
txt = 'My name is Timur, I am ' + str(age)
print(txt)
# Такой код работает, однако в Python предпочтительным
# способом форматирования считается использование метода format.
# Предыдущую программу можно переписать в виде:

age = 27
txt = 'My name is Timur, I am {}'.format(age)
print(txt)
# Мы передаем необходимые параметры методу format,
# а Python форматирует указанную строку и помещает их
# в строку на место заполнителей {}. Мы можем создавать
# сколько угодно заполнителей в строке:

age = 27
name = 'Timur'
profession = 'math teacher'
txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, profession)
print(txt)

print('используем ЗАПОЛНИТЕЛЬ!')

age = 27
name = 'Timur'
profession = 'math teacher'
txt = 'My name is {0}, I am {1}, I work as a {2}'.format(name, age, profession)
print(txt)

name = 'Timur'
txt = 'My name is {0}-{0}-{0}'.format(name)
print(txt)
# зполнитель может использоваться несколько раз.

first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print('Hello, {0} {1}. You are {2}. You are a {3}. You were a member of {4}'.format(first_name, last_name, age,
                                                                                    profession, affiliation))

first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. You were a member of {affiliation}')

# из комментов
num = 1000000.2345
print(f'{num:,.3f}')
# интересно, возможны ли другие разделителм

first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print(f'Hello, {first_name} {last_name}.'
      f' You are {age}. '
      f'You are a {profession}. '
      f'You were a member of {affiliation}')
# легкий перевод строки.

# import timeit
