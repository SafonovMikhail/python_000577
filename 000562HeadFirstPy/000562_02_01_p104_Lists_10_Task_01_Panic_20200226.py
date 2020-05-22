phrase = "Don't panic"
plist = list(phrase)
print(phrase)
print(plist)
print(len(plist))
new_phrase = []
for i in range(len(plist)):
    # print(plist[i])
    if plist[i] == 'o' or plist[i] == 'n' or plist[i] == 't' or plist[i] == 'p':
        print(plist[i])
        # new_phrase = new_phrase.pop(plist[i])

        # new_phrase = new_phrase.append(phrase(i))
# new_phrase = ''.join(plist)
# print(plist)
print(new_phrase)
