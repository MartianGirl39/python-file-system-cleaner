# This is a sample Python script.
import os.path

from clean import clean
import sys
import logging

def iterate_dir(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if os.path.isfile(entry.path):
                print(os.path.abspath(entry.path))
            elif os.path.isdir(entry.path) and os.path.basename(entry.path) != ".venv":
                iterate_dir(entry.path)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = sys.argv
    print(os.path.abspath(os.path.dirname(__file__)))
    iterate_dir(os.path.abspath(os.path.dirname(__file__)))
    # if args[1] == "delete":
    #     clean(args[len(args)-1], args[2:len(args)-1])
    # elif args[1] == "organize":
    #     pass

