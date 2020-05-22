'''

Another type in Python is the Boolean type.
There are two Boolean values: True and False.
They can be created by comparing values,
for instance by using the equal operator ==.

Be careful not to confuse assignment (one equals sign)
with comparison (two equals signs).
'''
print("000758_02_01_BooleanComparison:01")
my_boolean = True
print(my_boolean)
print(2 == 3)
print("hello" == "hello")

'''
What are the two Boolean values in Python?
() Truth and Falsity
() true and false
() True and False
'''

'''
Comparison

Another comparison operator, the not equal operator (!=), 
evaluates to True if the items being compared aren't equal, 
and False if they are.
'''
print("000758_02_01_BooleanComparison:02")
print(1 != 1)
print("eleven" != "seven")
print(2 != 0)
'''
What is the output of this code?
>>> 7 != 8
() True
() False
'''
'''
()
Python also has operators that determine whether one number (float or integer) 
is greater than or smaller than another. These operators are > and < respectively.
https://code.sololearn.com/caaZSBkJ3bhV
'''
print("000758_02_01_BooleanComparison:03")
print(7 > 5)
print(10 < 10)
'''
(q.03)
What is the output of this code?
>>> 7 > 7.0
'''
'''
(04)
The greater than or equal to, and smaller than or equal to operators are >= and <=.
They are the same as the strict greater than and smaller than operators, 
except that they return True when comparing equal numbers.
Greater than and smaller than operators can also be used to compare strings 
lexicographically (the alphabetical order of words is based on the alphabetical 
order of their component letters).
'''
print("000758_02_01_BooleanComparison:04")
print("too" > "to")
# is true as 3 letters is more than 2 letters.
print("sea" < "tea")
# is true as t comes after s in the alphabetical order.
print("a" < "d")
print("g" > "m")
print("ad" < "bc")
'''
ASCII table!
When comparing 2 characters in a boolean expression, 
python compares their ASCII codes (search in google). 
For the uppercase alphabet, 
A - Z, the values go from 65 to 90 and for 
the lowercase alphabet, a - z, the values go from 97 to 122. 
Now, it should be obvious why the above boolean expressions behave as they do.
'''
print("000758_02_01_BooleanComparison:04")
print("A" > "a")
print(65 > 97)
'''
the number 2 in the ASCII Table is 50.
'''
print("000758_02_01_BooleanComparison:05")
print("2" < "A")
print(50 < 65)  # The computer will read as:

print("000758_02_01_BooleanComparison:06")
a = 4 == 4
b = 3 != 3
c = 8 < 6
d = 5 <= 7
print("a =", a, "\nb =", b, "\nc =", c, "\nd =", d, "\nSum =", a + b + c + d)

print("000758_02_01_BooleanComparison:07")
print("too" > "to")
print("too" > "Too")
print("TOO" > "too")

'''
(q.03)
What is the output of this code?
>>> 8.7 <= 8.70
'''
print("000758_02_01_BooleanComparison:q:04")
print(8.7 <= 8.70)

