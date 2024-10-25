import pytest
import os
from clean import clean
from unittest.mock import patch

def create_test_dir():
    file_names = ["Resume_01", "Resume_01(1)", "Resume_02", "my-doggo", "A_Tale_Of_Two_Cities_Essay", "hello"]
    if not os.path.exists("./resources"):
        os.mkdir("./resources")
    else:
        clean("./resources", [])
    for i in range(0, 5):
        with open(f"./resources/{file_names[i]}.txt", "w") as file:
            file.write('This is for testing')
    if not os.path.exists("./resources/dir"):
        os.mkdir("./resources/dir")
        for i in range(0, 5):
            with open(f"./resources/dir/{file_names[i]}.txt", "w") as file:
                file.write('This is for testing')
    if not os.path.exists("./resources/resumes"):
        os.mkdir("./resources/resumes")

def test_delete_01():
    create_test_dir()
    clean("./resources", ["-i"])
    assert os.path.exists("./resources") == True and len(os.listdir("./resources")) == 5

def test_delete_02():
    create_test_dir()
    clean("./resources", ["-i"])
    assert os.path.exists("./resources/dir") and len(os.listdir("./resources/dir")) == 3

@patch('builtins.input', side_effect=['y', 'y', 'y', 'y', 'y', 'y', 'y'])
def test_delete_03(mock_input):
    create_test_dir()
    clean("./resources", ["-i", "prompt"])
    assert os.path.exists("./resources") == True and len(os.listdir("./resources")) == 0


