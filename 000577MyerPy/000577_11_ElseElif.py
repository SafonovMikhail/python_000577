# 000577_11_ElseElif.py
'''


'''
print("\n000577_11_ElseElif:part 01:var 01:")
species = "dog"
if species == "cat":
    print("Yep, it's cat.")
if species != "cat":
    print("Nope, not cat.")
'''
if there's no "cat"
'''
print("\n000577_11_ElseElif:part 01:var 02:")
if species == "cat":
    print("Yep, it's cat.")
else:
    print("Nope, not cat.")
'''
The keyword else gets its own line and a colon at the end.
Statements that execute in the else case are indented.
As in the if case, any number of statements can execute in the else

Finally, there's elif. It's short for else if. If no test has been successful yet,
an elif tries something else.
'''
print("\n000577_11_ElseElif:part 02:")
donut_condition = "not fresh"
donut_price = "high"
if donut_condition == "fresh":
    buy_score = 10
elif donut_price == "low":
    buy_score = 5
else:
    buy_score = 0
print("buy_score:", buy_score)
'''
Since an else statement is a catchall, you would never have more than one
of them. It always comes last, stipulating what happens if all tests have failed.
'''
print("\n000577_11_ElseElif:part 03:")
donut_condition = "_"
donut_filling = "chocolate"
donut_price = ""
buy_score = 0
if donut_condition == "fresh":
    buy_score += 10
if donut_filling == "chocolate":
    buy_score += 5
if donut_price == "reasonable":
    buy_score += 7
print(buy_score)
'''
Exercise 1
Code line 3.
1 if species == "cat":
2  print("Yep, it's cat.")
3 __________
4   print("Nope, not cat.")
Solution:
else:


'''
print("\n000577_11_ElseElif_Ex01:")
if species == "cat":
    print("Yep, it's cat.")
else:
    print("Nope, not cat.")
'''
Exercise 2
If the condition tested in line 1 fails, line 3 tests for a different condition. What keyword goes in the blank?
1 if donut_condition == "fresh":
2   buy_score = 10
3 ____ donut_price == "low":
4   buy_score = 5
5 else:
6   buy_score = 0
'''
print("\n000577_11_ElseElif_Ex02:")
print(donut_condition)
if donut_condition == "fresh":
    buy_score = 10
elif donut_price == "low":
    buy_score = 5
else:
    buy_score = 0
    print(buy_score)
'''
Exercise 3
Code the next line that says what to do if the test fails.
if a == b:
   print("a equals b")
Solution: else:

Exercise 4
Code the next line. If a doesn't equal b, test whether c equals d.
if a == b:
   print("a equals b")
Solution: 
elif c == d:
'''
print("\n000577_11_ElseElif_Ex04:")
a = 1
b = 2
c = 3
d = 3
if a == b:
    print("a equals b")
elif c == d:
    print("c equals d")
'''
Exercise 5
Code four lines. If a equals b, c equals d. If the test fails, e equals f.
Solution:
if a == b:
  c = d
else:
  e = f
Замечание: не equals, а присвоить значение. Это разные поняти.
'''
print("\n000577_11_ElseElif_Ex05:")
f = 4
if a == b:
    c = d
else:
    e = f
print(e)
'''
Exercise 6
Code four lines. 
If a equals b, c equals d. If that test fails, then if e equals f, g equals h.
'''
print("\n000577_11_ElseElif_Ex06:")
g = ""
h = "h"
print(a, b, c, d, e, f, g, h, sep="___", end="~~~")
e = 1
d = 1
if a == b:
    c = d
elif e == d:
    g = h
print("\n" + g)
'''
Exercise 7
What is the value of x?
if 2 + 3 == 4:
  x = 0
elif 2 - 1 == 1:
  x = 1
elif 3 + 3 == 6:
  x = 2
else:
  x = 3
'''
print("\n000577_11_ElseElif_Ex07:")
if 2 + 3 == 4:
    x = 0
elif 2 - 1 == 1:
    x = 1
elif 3 + 3 == 6:
    x = 2
else:
    x = 3
print("x =", x)
'''
Exercise 8
Code the next two lines. 
If the test fails, test if a equals 2. If so, display "a equals 2".
if a == 1:
  print("a equals 1")
'''
print("\n000577_11_ElseElif_Ex08:")
print(a)
if a == 1:
    print("a equals 1")
elif a == 2:
    print("a equals 2")
'''
Exercise 9

Code the next two lines. If the first two tests fail, display "failed".
if a == b:
  print("ok")
elif c == d:
  print("ok")

(!!!) предлагает решать с помощью else, но ведь без него можно и обойтись
но не все так гладко получилось в примере 10, у меня отпечаталось 2 раза.
'''
print("\n000577_11_ElseElif_Ex09:")
print(a, b, c, d, sep="____")
if a == b:
    print("ok")
elif c == d:
    print("ok")
print("failed")
'''
Exercise 10
Code six lines. 
If a equals b, display "ok". 
If not, then 
if c equals d, 
display "ok". 
If both tests fail, 
display "failed".
'''
print("\n000577_11_ElseElif_Ex10:")
print(a, b, c, d, sep="____")
d = 3
if a == b:
    print("ok")
elif c == d:
    print("ok")
else:
    print("failed")
'''
Exercise 11
Display wrong if the condition isn't met.
https://trinket.io/python3/c9c7999683
if "dog" == "cat":
  print ("That's crazy")
On the next two lines, display "wrong" if the condition isn't met.
Solution:
https://trinket.io/python3/7dfe75a209
'''
print("\n000577_11_ElseElif_Ex11:")
if "dog" == "cat":
  print ("That's crazy")
# On the next two lines, display "wrong"
# if the condition isn't met.
else:
  print ("wrong")
'''
Exercise 12
If the first condition isn't met, test whether "cat" equals "cat." If so display ok
https://trinket.io/python3/e7b102876c
if "dog" == "cat":
  proposition = "crazy"
# On the next two lines, if the condition above isn't met,
# test whether "cat" is equal to "cat"
# If so, display "ok"
Solution:
https://trinket.io/python3/37f7631151
'''
print("\n000577_11_ElseElif_Ex12:")
if "dog" == "cat":
  proposition = "crazy"
# On the next two lines, if the condition above isn't met,
# test whether "cat" is equal to "cat"
# If so, display "ok"
elif "cat" == "cat":
  print ("ok")


'''
print("\n000577_11_ElseElif_Ex??:")
animal = "mouse"
if animal == "dog" or "cat" or "mouse":
    print("mammal")
'''
