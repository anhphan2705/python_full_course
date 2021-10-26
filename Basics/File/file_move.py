import os

source = "C:\\Users\\black\Desktop\\Study\\Python\\Learning\\File\\text.txt"
destination = "C:\\Users\\black\\Desktop\\Study\\Python\\Learning\\Other\\Test\\text.txt"

try:
    if os.path.exists(destination):
        print("There is already a file with the same name")
    else:
#os.replace(source, destination) = move file from source to new destination
        os.replace(source, destination)
        os.replace(destination, source) #Intended to return the file back for other lesson 
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")