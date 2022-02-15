'''
Python has several functions for creating, reading, updating, and deleting
files.
    The key function for working with files in Python is the open() function.
    There are four different methods (modes) for opening a file:
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists
'''

try:
    f = open("D:\Python\File_Handling\sample_file.txt", "r") #it will open the file in read mode
    print(f.read())
except:
    print('Error in accessing the file!')
else: #if there is no exception else will work
    print('Successful read')