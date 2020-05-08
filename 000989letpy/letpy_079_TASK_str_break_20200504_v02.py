string = input()
j = 0
while j + 1 < len(string):
    if string[j] == '#' and string[j + 1] == '#':
        break
    elif string[j] != '#':
        print(string[j])
    j += 1
    if j == len(string):
        break

# asdlgkjawig##agkjaslk
# asdlgkjawi#gagkjaslk#
# asdlgkjawigagkjaslk#
