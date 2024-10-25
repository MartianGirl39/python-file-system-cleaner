import os
import re
import shutil

from requests.packages import target

from clean.handlers.basic import basic_delete_handler
from organize.handlers.helpers import retrieve_from_resources, get_absolute_path

def basic_handler_factory(context, is_recursive, recursion_option):
    word_bank = retrieve_from_resources("smart-word-bank.txt")
    file_context = context

    def is_keyword(file_name):
        words = re.split(r'\s+|-|_', file_name)
        for index, item in enumerate(words):
            for word in word_bank:
                if word in item.lower():
                    return word, index
        return "", -1

    def find_file_type(extension):
        for key in file_context.keys():
            if extension in file_context.get(key):
                return key
        return ""

    def create_directory(path):
        if not os.path.exists(path):
            os.mkdir(path)

    def move_file(abs_path, target_path):
        print(f"dir is {os.path.dirname(abs_path)}, targeat is {os.path.abspath(target_path)}")
        if not os.path.exists(f"{target_path}/{os.path.basename(abs_path)}"):
            shutil.move(abs_path, target_path)
        elif os.path.dirname(abs_path) == os.path.abspath(target_path):
            print("do nothing")
        else:
            file_name = os.path.basename(abs_path)
            intersection = file_name.find(".")
            extension = file_name[intersection + 1:]
            path = target_path
            index = 1
            while index < 20:
                target_path = f"{path}/{file_name[:intersection]}({index}).{extension}"
                print(f"target path is {target_path}")
                if not os.path.exists(f"{target_path}/{os.path.basename(abs_path)}"):
                    shutil.move(abs_path, target_path)
                    break
                index += 1

    def process_file(path, uplift = ""):
        if os.path.isfile(path):
            abs_path = os.path.abspath(path)
            file_name = os.path.basename(path)
            intersection = file_name.find(".")
            extension = file_name[intersection + 1:] if intersection != -1 else ""
            file_path = os.path.dirname(abs_path)
            base_name = file_name[:intersection]

            keyword_match, index = is_keyword(base_name)
            if keyword_match:
                target_dir = f"{file_path}/{word_bank[index]}"
                if not uplift == "":
                    target_dir = f"{uplift}/{word_bank[index]}"
                create_directory(target_dir)
                move_file(abs_path, target_dir)
            else:
                file_type = find_file_type(extension)
                target_dir = f"{file_path}/{file_type}"
                if not uplift == "":
                    target_dir = f"{uplift}/{file_type}"
                print(f"uplift is {uplift}")
                create_directory(target_dir)
                move_file(abs_path, target_dir)

    def process_directory(path):
        with os.scandir(path) as entries:
            for entry in entries:
                if recursion_option == "sort":
                    basic_delete_handler(entry.path)
                elif recursion_option == "uplift":
                    process_file(entry.path, os.path.dirname(path))
        if len(os.listdir(path)) < 1:
            os.rmdir(path)

    def basic_handler(path):
        if os.path.isfile(path):
            process_file(path, "")
        elif os.path.isdir(path) and is_recursive:
            process_directory(path)

    return basic_handler
