from os.path import abspath, join, dirname

def get_absolute_path(file_name):
    my_path = abspath(dirname(__file__))
    return join(my_path, f"../../resources/{file_name}")

def retrieve_from_resources(file_name):
    words = []
    path = get_absolute_path(file_name)
    with open(path, "r") as file:
        words = file.readline().split("|")
    return words