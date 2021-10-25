try:
#with open(file_name) as file = open a file and store is as variable file. Uses file_name when the file is in the same folder
#with open(file_path) as file = open a file and store is as variable file
    with open("C:\\Users\\black\\Desktop\\Study\\Python\\Learning\\Other\\Test\\test.txt") as file:
#file.read() = read the file
        print(file.read())
except FileNotFoundError:
    print("File was not found")
#file.closed = return true or false whether the file is closed
#print(file.closed) 