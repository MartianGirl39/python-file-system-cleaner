import os
from .helpers import prompt, clean_directory


def safe_delete_handler(path):
    if os.path.isfile(path):
        string = f"Do you want to delete file ${path} of size ${round(os.path.getsize(path) / 1024 ** 2)}mb"
        if prompt(string):
            os.remove(path)
            return 1
        else:
            print(f"File ${path} skipped")
            return 0
    elif os.path.isdir(path):
        return clean_directory(path, safe_delete_handler)
    else:
        print(f"Could not process item at ${path}")
        return 0

