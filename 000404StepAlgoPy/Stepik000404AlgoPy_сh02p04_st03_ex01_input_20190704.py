a=int(input())
b=int(input())
c=float(input())
print('sum (a + b) =',a+b)
print('sum (a + c) =',a+c)
print('(a)', type(a))
print('(b)', type(b))
print('(c)', type(c)) # определение типа введенной переменной
s=input().split() # ввод последовательности, разделенной пробелами
#данные для ввода: [ a  b c   d  ]
print(s)
s=list(map(int,input().split())) # ввод списка раздельных целых значений
#данные для ввода: [23   45       98   21       34]
print (s)
print ('input number of elements')
n=int(input())
a=[int(input()) for _ in range(n)] #заполнение списка через последовательное введение чисел
print (a)
print ('input number of elements')
n=int(input())
a = [input("Введите {}: ".format(i)) for i in range(n)]
print (a)
print ('input number of elements')
n = int(input())
a = [int(input(f'{i+1}: ')) for i in range(n)]
print(a)
print ('ниже ошибочный код')
print ('input number of elements')
n = int(input())
a=[int(input(i) for i in range(n))] #в курсе можно предложить править в качестве задания

