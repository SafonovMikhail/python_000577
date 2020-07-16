'''
[+-]
https://qna.habr.com/answer?answer_id=1653005
'''


def check(arr):
    while arr == sorted(arr):
        print('по росту')
        return
    print('не по росту')


print(check([1, 2, 3]))
