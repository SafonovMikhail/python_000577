'''
https://qna.habr.com/answer?answer_id=1653027
'''
h1 = int(44)
h2 = int(45)
h3 = int(46)

my_dict = {True: 'По росту', False: 'Не по росту!'}
my_list = [h1, h2, h3]
print(my_dict.get(my_list == sorted(my_list)))
