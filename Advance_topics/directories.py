from pathlib import Path


'''
There are two ways to add path

Absolute path: We start from the root of our hardisk
eg: c:\Program Files\Microsoft

Relative path: It works from the current directory
'''
path1=Path("Conditions_and_Loops") #if we don't pass an argument, it will refer to current directory
path2=Path("disk1")
print(path1.exists()) #it returns a boolean value
print(path2.exists()) 