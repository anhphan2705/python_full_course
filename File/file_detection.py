import os

#Declaring the path of the file
path_1 = "C:\\Users\\black\\Desktop\\Study\\Python\\Learning\\Other\\Test"
path_2 = "C:\\Users\\black\\Desktop\\Study\\Python\\Learning\\Other\\Test\\test.txt"

#os.path.exist(path) = Checking if the path exist
if os.path.exists(path_1):
    print("That location exists")
#os.path.isfile(path) = Checking if the path leads to a file
    if os.path.isfile(path_1):
        print("That is a file")
#os.path.isdir(path) = Checking if the paht leads to a directory/folder
    if os.path.isdir(path_2):
        print("That is a directory")
else: 
    print("That location doesn't exist")