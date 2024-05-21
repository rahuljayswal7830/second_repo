from os import path
from pathlib import Path
from zipfile import ZipFile
import os
import time

#****************dir name 
dir_name="python-job"

#*********** first check folder 
if not os.path.exists(dir_name):
    os.mkdir(dir_name)




#*************file path
# file_path=os.path.join(dir_name,"a.txt")
with open(f"{dir_name}/a.text","w") as file:
    file.write("this is fake downments\n")
    file.write("we are using only for enjoy\n")

# file_path=os.path.join(dir_name,"b.txt")
with open(f"{dir_name}/b.text","w") as file:
    file.write("this is fake downments\n")
    file.write("we are using only for enjoy\n")


print(os.path.isfile(f"{dir_name}/a.text"))
print(os.path.isdir(dir_name))


# file_path=os.path.join(dir_name,"zip.zip")
with ZipFile(f"{dir_name}/zip.zip",mode="w") as zipfile:
    for file in os.listdir(dir_name):
        print(file)
        zipfile.write(os.path.join(os.path.curdir,f"{dir_name}/{file}"))

time.sleep(30)
for file in os.listdir(dir_name):
    print(os.path.curdir)
    os.remove(os.path.join(os.path.curdir,f"{dir_name}/{file}"))

time.sleep(30)
if os.path.exists(dir_name):
    os.rmdir(dir_name)


