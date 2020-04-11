#Returns the current working directory.
#It’s like a one liner to your house address
import os
print(os.getcwd())
#Return the real group id of the current process.
# print(os.getgid())

#Return the current process’s user id.
#Process is like the life of a program
# print(os.getuid())

#Returns the real process ID of the current process.
print(os.getpid())

#Create a directory named path with numeric mode mode.
# os.mkdir('path')

#repetitive directory creation function.
# os.makedirs('path1')

#Remove (delete) the file path.
# os.remove('path')

#Remove directories recursively.
# os.removedirs(path)

#Rename the file or directory src to dst.
# os.rename(src, dst)

#Remove (delete) the directory path.
# os.rmdir(path)
