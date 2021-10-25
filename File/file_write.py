
#open("file_name", "w") = open up a file in writing mode
#w = write, r = read, a = append
with open("C:\\Users\\black\\Desktop\\Study\\Python\\Learning\\File\\text.txt", 'w') as file:
    file.write("bananaan")

with open("C:\\Users\\black\\Desktop\\Study\\Python\\Learning\\File\\text.txt", 'a') as file:
    file.write("bananaan number 1")