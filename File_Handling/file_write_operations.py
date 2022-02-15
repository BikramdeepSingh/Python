'''
To write to an existing file, we must add a parameter to the open() function:
"x" - Create - will create a file, returns an error if the file exist
"a" - Append - will append to the end of the file, will create a file if the specified file does not exist
"w" - Write - will overwrite any existing content, will create a file if the specified file does not exist
'''

try:
    f = open("D:\Python\File_Handling\Auto_creation.txt", "w") #it will open the file in read mode
    f.write("Oops! This was written using write method")
    
except:
    print('Error in accessing the file!')
else: #if there is no exception else will work
    print('Successful write')
finally:
    f.close()
    print('Closed the file successfully')