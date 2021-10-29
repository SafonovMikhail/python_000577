# 001711v05t00500
import random


def main():
    while True:
        random_number = random.randint(0, 10)
        user_number = int(input('input num'))
        if user_number == random_number:
            print('win')
        else:
            print('loose')
        answer = input('more?')

# main()

if __name__ == "__main__":
# print('hi')
    main()
