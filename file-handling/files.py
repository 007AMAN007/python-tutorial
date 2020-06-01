#File handling is an important part of any web application.

#Python has several functions for creating, reading, updating, and deleting files.

#The key function for working with files in Python is the open() function.

#The open() function takes two parameters; filename, and mode.

#There are four different methods (modes) for opening a file:

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists


#read files

# f = open("demo.txt","r") #open with read

# print(f.read()) #read file

# print(f.read(5)) #read 5 chars of file

# print(f.readline()) #read 1 line of file

# print(f.readlines()) #read all lines of file

# f.close() #close file

#write file

# f = open("demo.txt", "a") #write mode
# f.write("Now the file has more content!") #wite files
# f.close() #close

#overwrite the content:
# f = open("demo.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

#delete file
# for delete file we have to import "os" module

# import os
# os.remove("demofile3.txt")

#Remove the folder "myfolder":

# import os
# os.rmdir("myfolder")