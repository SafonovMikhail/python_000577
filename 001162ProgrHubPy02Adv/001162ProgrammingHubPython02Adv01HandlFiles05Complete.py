# write to file
text = 'Donald trump runs for president'
# Creates Presidency.txt
saveFile = open('Presidency.txt', 'w')
# Writes text to Presidency.txt
saveFile.write(text)
print('File Created : Presidency.txt')
saveFile.close()
# append from file
appendME = 'Donald trump is elected president of United states of America'
# Opens in append mode
appendFile = open('Presidency.txt', 'a')
