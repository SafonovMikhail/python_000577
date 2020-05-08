n = int(input())
if n == 1:
    print(n)
else:
    sum1 = 1
    sum2 = 1
    print(sum1, sum2, end="")
    for i in range(1, n - 1):
        sum3 = sum2 + sum1  # 1 + 0;    1 + 1 = 2;
        sum1 = sum2  # 1         2
        sum2 = sum3  # 1         2
        print("", sum3, end="")
        # if n == 1:
        #     print("1", " ", end='')
        # else:
        #     print("1", " ", end="")
        #     sum1 += i
        #     print(str(sum1), end='')
