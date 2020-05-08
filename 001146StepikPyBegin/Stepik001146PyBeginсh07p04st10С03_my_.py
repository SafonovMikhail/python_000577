word1 = input()
count1 = 0
while (word1 != "стоп") and (word1 != "хватит") and (word1 != "достаточно"):
    # print(word1)
    count1 += 1
    word1 = input()
print(count1)
