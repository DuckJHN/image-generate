import os

def check_folder_or_create(path):
    is_exist = os.path.exists(path)
    if not is_exist:
        os.makedirs(path)
    return path
