# from pathlib import Path
# import time
# from zipfile import ZipFile
# dir_path=Path("python-lab")

# if not dir_path.exists():
#     dir_path.mkdir()



# file_path=dir_path / "a.txt"

# with open(file_path,"w") as file:
#     file.write("random file \n")


# file_path=dir_path / "b.txt"

# with open(file_path,"w") as file:
#     file.write("random file \n")


# with ZipFile(f"{dir_path}/zip.zip",mode="w") as zip_file:
#     for file in dir_path.iterdir():
#         zip_file.write(file)

# time.sleep(5)
# with ZipFile(f"{dir_path}/zip.zip",mode="r") as zip_file:
#     zip_file.extractall(f"{dir_path}")

# print(file_path.is_file())
# print(file_path.is_dir())

# print(dir_path.is_dir())


# print(file_path.parent)

# time.sleep(30)
# for file in dir_path.iterdir():
#     file.unlink()

# time.sleep(30)
# dir_path.rmdir()


import json

import datetime
date=datetime.datetime.now().strftime("%Y-%m-%d")

date=1.25
print(date)

string=json.dumps(date)

print(string)
print(type(string))

date=json.loads(string)
print(date)
print(type(date))