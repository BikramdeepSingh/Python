'''
To write to an existing file, we must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
'''

try:
    f = open("D:\Python\File_Handling\sample_file.txt", "a") #it will open the file in read mode
    f.write("This was written using append method")
    
except:
    print('Error in accessing the file!')
else: #if there is no exception else will work
    print('Successful write')
finally:
    f.close()
    print('Closed the file successfully')