str = 'Hello'
print("id(str): ", id(str))
print(str.upper())
print(id(str.upper()), id(str))
str = str.upper()
print("id(str): ", id(str))

# [.upper] - пример вызова у строковго литералла
print('upper'.upper())

print("# подсчет [.count] числа вхождений [ra]: ")
msg = "abrakadabra"
print("ra:", msg, msg.count("ra"))
print(msg.count("ra", 4, 10))
print(msg.count("ra", 4, 11))

print()
print("# индекс первого [.find] вхождения [br]: ")
print(msg.find("br"))

print()
print("# индекс первого вхождения [.rfind] в обратном порядке [br]: ")
print("len(msg): ", len(msg))
print(msg.rfind("br"))

print()
print("# замена [.replace] символов [a] на [o] : ")
print(msg.replace('a', 'o'))

print(msg.isalpha())
print('hello world'.isalpha())