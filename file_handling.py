from os import path
from pathlib import Path


directory_path= "take"
path_obj=Path(directory_path)
if not path_obj.exists():
    path_obj.mkdir()
else:
    print("directory already exists...")



file_path=path_obj.joinpath("an.py")

print(file_path.is_file())
print(file_path.parent)

print(path_obj.is_dir())

for i in path_obj.iterdir():
    print(i.name)




    