import os

from .helpers import clean_directory


def basic_delete_handler(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        return clean_directory(path, basic_delete_handler)
    else:
        print(f"Could not process item at ${path}")
        return 0
    return 1