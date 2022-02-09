from pathlib import Path


'''
There are two ways to add path

Absolute path: We start from the root of our hardisk
eg: c:\Program Files\Microsoft

Relative path: It works from the current directory
'''
path1=Path("Conditions_and_Loops") #if we don't pass an argument, it will refer to current directory
path2=Path("test_directory")
print(path1.exists()) #it returns a boolean value
print(path2.exists()) 

# path2.mkdir() # creates a new directory i.e. make directory
# print('New test directory made:',path2.exists())

# path2.rmdir()#it deletes a directory with the given name i.e. remove directory
# print('New test directory:',path2.exists())

path3=Path()#current directory

for file in path3.glob('*'):
    print(file) #prints every directory and files
#we can optionally add an extension but with that we will only get files 
#not the directories i.e. print(path3.glob('*.*'))