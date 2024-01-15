import os


def check_folder_or_create(path):
    is_exist = os.path.exists(path)
    if not is_exist:
        os.makedirs(path)
    return path


def check_folder_exist(path):
    if not os.path.exists(path):
        raise os.error("Folder not found.")
    return True
