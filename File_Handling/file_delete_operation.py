'''
To delete a file, you must import the OS module, and run its os.remove() function
'''
import os


try:
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")  
except:
    print('Error in accessing the file!')
else: #if there is no exception else will work
    print('Successful file deletion')
