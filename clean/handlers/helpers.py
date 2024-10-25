from os.path import abspath, join, dirname
import os

def get_absolute_path(file_name):
    my_path = abspath(dirname(__file__))
    return join(my_path, f"../../resources/{file_name}.txt")

def retrieve_from_resources(file_name):
    words = []
    path = get_absolute_path(file_name)
    with open(path, "r") as file:
        words = file.readline().split("|")
    return words

def check_word(answer):
    ## will eventually check if word can mean yes just in case
    pass

def append_to_resources(answer, file_name):
    path = get_absolute_path(file_name)
    with open(path, "a") as file:
        file.write('|' + answer)

def find_answer_meaning(answer):
    ans = input("Our system did not recognize your answer, could you please enter whether you meant this as yes or no by using y or yes for yes or n or no for no?").lower()
    if ans == "y" or ans == "yes":
        append_to_resources(answer, "affirmatives")
        return True
    elif ans == "n" or ans == "no":
        append_to_resources(answer, "negatives")
        return False
    else:
        print("Alright, be funny why dontcha!?")
        exit(1)

def __init_prompt():
    affirmatives = retrieve_from_resources("affirmatives")
    negatives = retrieve_from_resources("negatives")
    def new_prompt(string):
        if not string.find(":") == len(string)-1:
            string += ":"
        answer = input(string).lower()
        if answer == "y" or answer in affirmatives:
            return True
        elif answer == "n" or answer in negatives:
            return False
        else:
            is_affirmative = find_answer_meaning(answer)
            if is_affirmative:
                affirmatives.append(answer)
            else:
                negatives.append(answer)
            return is_affirmative
    return new_prompt

def clean_directory(path, handler):
    deleted = 0
    with os.scandir(path) as entries:
        for entry in entries:
            deleted += handler(entry.path)
    if len(os.listdir(path)) == 0:
        os.rmdir(path)
    return deleted

prompt = __init_prompt()

remove = os.remove

def format_options(options):
    parsed = {}
    lst = options
    keys = [item for item in lst if item[0] == "-"]
    for key in keys:
        parsed[key] = []
        start = lst.index(key) + 1
        for item in lst[start: ]:
            if item[0] == "-":
               break
            parsed[key].append(item)
    return parsed

def exists(path):
    return os.path.exists(path)

def is_directory(path):
    return os.path.isdir(path)

def delete(path, handle_delete):
    if exists(path):
        return handle_delete(path)
    else:
        pass
