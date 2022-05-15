
'''
Data file's absolute path: 
/home/dean/Documents/inventwithcode/Notes/python/Day - 24 - Files Directories and Paths/main.py

This file's absolute path: 
/home/dean/Desktop
'''
with open("../../../../../Desktop/data.txt", "w") as file:
    content = "Hello world, I am a Winchester!"
    file.write(content)

print("Your file has been created in Desktop Folder")
