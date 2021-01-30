# isalnum()
print('isalnum()')
s1 = 'abc123'
s2 = 'abc$*123'
s3 = ''

print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print()

# isalpha()
print('isalpha()')
s1 = 'ABCabc'
s2 = 'abc123'
s3 = ''

print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())
print()

# isdigit()
print('isdigit()')
s1 = '1234567'
s2 = 'abc123'
s3 = ''

print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())
print()

# islower()
print('islower()')
s1 = 'abc'
s2 = 'abc1$d'
s3 = 'Abc1$D'

print(s1.islower())
print(s2.islower())
print(s3.islower())
print()

print('isupper()')

s1 = 'ABC'
s2 = 'ABC1$D'
s3 = 'Abc1$D'

print(s1.isupper())
print(s2.isupper())
print(s3.isupper())
print()

print('isspace()')

s1 = '       '
s2 = 'abc1$d'

print(s1.isspace())
print(s2.isspace())
