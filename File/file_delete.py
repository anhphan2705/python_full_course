import os
import shutil

try:
#os.remove(path) = remove file in that path
    path = "C:\\Users\\black\\Desktop\\Study\\Python\\Learning\\File\\test.txt"
    os.remove(path)
#os.rmdir(path) = delete an empty directory
    #os.rmdir(path)
#shutil.rmtree(path) = delete a directory containing files #DANGEROUS
    #shutil.rmtree(path)
except FileNotFoundError:
    print("File not found")   
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete " + path + " using that function")
else:
    print(path + " was deleted")