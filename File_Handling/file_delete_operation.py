'''
To delete a file, you must import the OS module, and run its os.remove() function
To delete an entire folder, use the os.rmdir() method
'''
import os


try:
    if os.path.exists("D:\Python\File_Handling\demofile.txt"):
        os.remove("D:\Python\File_Handling\demofile.txt")
    else:
        print("The file does not exist")  
except:
    print('Error in accessing the file!')
else: #if there is no exception else will work
    print('Successful file deletion')
