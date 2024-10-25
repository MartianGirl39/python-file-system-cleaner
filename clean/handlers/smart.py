from os import scandir

from .basic import basic_delete_handler
from .safe import safe_delete_handler
from .helpers import retrieve_from_resources, prompt, clean_directory
import os
import re

def smart_delete_handler_factory(is_safe, args):
    with_prompt = False
    if args == "prompt":
        with_prompt = True

    word_bank = retrieve_from_resources("smart-word-bank")
    previous = []

    child_handler = basic_delete_handler
    if is_safe:
        child_handler = safe_delete_handler

    def is_duplicate(file_name):
        for name in previous:
            if name in file_name:
                return True
        return False

    def is_important(file_name):
        words = re.split('/s+|-|_', file_name)
        for item in words:
            for word in word_bank:
                if word in item.lower():
                    return True
        return False

    def smart_delete_handler(path):
        max_length = 1000
        max_size = 20
        ## check if it is a file
        if os.path.isfile(path):
            file = os.path.basename(path)
            end = file.find(".")
            if end < 0:
                end = len(file)
            file = file[:end]
            if is_duplicate(file):
                return child_handler(path)
            elif (not round(os.path.getsize(path) / 1024 ** 2) > max_length and not is_important(file.lower())) or (
                with_prompt and prompt(f"file {path} might be important, would you like use to ignore this file?")):
                return child_handler(path)
            previous.append(file)
        elif os.path.isdir(path):
            print(f"directory is {os.path.basename(path)}")
            if(not len(os.listdir(path)) > max_size and not is_important(os.path.basename(path).lower())) or (
                with_prompt and prompt(f"directory {path} might be important, would you like us to skip over this directory?")):
                return clean_directory(path, smart_delete_handler_factory(is_safe, args))
        return 0

    return smart_delete_handler