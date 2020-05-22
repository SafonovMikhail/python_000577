# 40_How to get information out of a dictionary within another dictionary
customers = {
    0: {
    "first name": "John",
    "last name": "Ogden",
    "address": "301 Arbor Rd.",
        },
    1: {
    "first name": "Ann",
    "last name": "Sattermyer",
    "address": "PO Box 1145",
        },
    2: {
    "first name": "Jill",
    "last name": "Somers",
    "address": "3 Main St.",
        },
}
# Как вывести на печать массив не в одну строку, а вертикально, так, как его удобнее воспринимать
print(customers[2]["address"])   # сразу, как будто слепота. В каких скобках обращаться к словарю 2?
# Если не усвоил, не посчитал нужным обратить должное внимание,
# просто упустил из виду, таким образом, что нужно мне самому сделать в качестве учебной нагрузки, чтобы прописать в сознании, что реально должно быть, каков должен быть синтаксис

