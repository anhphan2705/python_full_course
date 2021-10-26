#copyfile() = copy the content of a file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)

import shutil
#shutil.copyfile(source path, destination path)
#shutil.copy(source path, destination path)
#shutil.copy(source path, destination path)
shutil.copyfile("test.txt", "copy.txt")  
