#append from file
#String to append to the file
question = 'What\'s the difference between a pizza and my pizza jokes?\n'
#Appends after question
answer = 'My pizza jokes can\'t be topped\n'
#Opens puns.txt
appendFile = open('puns.txt','a')
#Appends question variable
appendFile.write(question)
#Appends answer variable
appendFile.write(answer)
appendFile.close()