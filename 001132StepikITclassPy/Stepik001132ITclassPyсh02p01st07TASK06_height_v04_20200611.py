'''
https://qna.habr.com/q/790553
'''
h1 = int(input())
h2 = int(input())
h3 = int(input())

result = ['Не по росту!', 'По росту!']
compare = h1 <= h2 <= h3
print(result[compare])
