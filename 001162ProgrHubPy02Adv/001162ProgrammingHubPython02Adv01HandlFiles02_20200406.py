 #write to file
text = 'Ask your pizza delivery guy for a joke, and he\'ll deliver'
text02 = '\ncreated by: 001162ProgrammingHubPython02Adv01HandlFiles02.py'
#creates a file named puns.txt
saveFile = open('puns.txt','w')
#writes content of text variable to the file
saveFile.write(text)
saveFile.write(text02)
#closes the file
saveFile.close()