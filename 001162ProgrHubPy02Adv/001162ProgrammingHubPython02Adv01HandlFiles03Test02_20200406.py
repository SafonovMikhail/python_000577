file_var = open('file.txt', 'w')
file_var.write('first\n')
file_var.write('second\n')
file_var.close()
appendFile = open('file.txt', 'a')
# for i in 10:
# appendFile.write('\nsome text %s' % i)
appendFile.write('some text')
appendFile.close()
