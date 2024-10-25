# there should be multiple options for deletion
import sys
import os
from .handlers.helpers import is_directory, format_options, delete as try_delete
from .handlers.basic import basic_delete_handler
from .handlers.safe import safe_delete_handler
from .handlers.smart import smart_delete_handler_factory

def get_handler(is_smart, is_safe, options):
    if is_smart:
        return smart_delete_handler_factory(is_safe, options)
    if is_safe:
        return safe_delete_handler
    return basic_delete_handler

def is_match(orders, pattern, path):
    if "case_insensitive" in orders:
        path = path.lower()
        pattern = pattern.lower()
    if "contains" in orders:
        return pattern in path
    elif ("starts-with" in orders or "begins-with" in orders) and "ends-with" in orders:
        start = path.find(".")
        if start == -1:
            start = len(path)
        return path.startswith(pattern) or path[:start].endswith(pattern)
    elif "starts-with" in orders or "begins-with" in orders:
        return path.startswith(pattern)
    elif "ends-with" in orders:
        return path.endswith(pattern)
    else:
        raise ValueError("Invalid argument for orders")


### DELETE ALL
def delete(path, is_smart, is_safe, option):
    handler = get_handler(is_smart, is_safe, option)
    deleted = 0
    with os.scandir(path) as entries:
        for entry in entries:
            deleted += try_delete(entry.path, handler)
    print(f"A total of ${deleted} items were deleted successfully")


### DELETE BY MATCH
def regex_delete(path, orders, pattern, is_smart, is_safe, option):
    handler = get_handler(is_smart, is_safe, option)
    deleted = 0
    with os.scandir(path) as entries:
        for entry in entries:
            if is_match(orders, pattern, entry.name):
                deleted += try_delete(entry.path, handler)
    print(f"A total of ${deleted} items were deleted successfully")
    return deleted

##
def clean(directory, options):
    lists = []
    ## drives the entire program for deleting
    ## delete command goes like this py-clean clean [options] parent_directory -> -s = safe, -i = intelligent, -p = patterns, -o = orders
    if not is_directory(directory):
        print("Last argument must be a valid directory path")
        sys.exit(0)
    parsed = format_options(options)
    safe_option = ""
    if "-i" in parsed and "prompt" in parsed.get("-i"):
        safe_option = "prompt"
    print(safe_option)
    if "-p" in parsed:
        if not "-o" in parsed:
            parsed["-o"] = ["contains", "case_insensitive"]
        return regex_delete(directory, parsed.get("-o"), parsed.get("-p")[0], "-i" in parsed, "-s" in parsed, safe_option)
    return delete(directory, "-i" in parsed, "-s" in parsed, safe_option)


def main():
    print("Running the cleaning process...")
    args = sys.argv
    if len(args) > 1:
        clean(args[1], args[2:])
    else:
        print("Failed, please supply a path")

if __name__ == "__main__":
    main()
