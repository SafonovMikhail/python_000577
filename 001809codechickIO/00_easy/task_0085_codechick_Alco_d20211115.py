'''

'''


def should_serve_drinks(age, on_break):
    if age >= 18 and on_break == False:
        return True
    else:
        return False


print(should_serve_drinks(17, False))
