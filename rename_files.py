import os


def rename_files():
    path = r"C:\Users\xjy\Downloads\prank"
    file_list = os.listdir(path)
    cwd = os.getcwd()
    print("Current working directory is " + cwd)
    os.chdir(path)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans("", "", "0123456789")))
    os.chdir(cwd)


rename_files()
