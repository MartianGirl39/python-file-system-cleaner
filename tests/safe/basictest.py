import pytest
import os
from unittest.mock import patch
from clean import clean

def create_test_dir():
    if os.path.exists("./resources"):
        clean("./resources", [])
    else:
        os.mkdir("./resources")
    for i in range(0, 3):
        with open(f"./resources/test-{i}.txt", "w") as file:
            file.write('This is for testing')
    if not os.path.exists(f"./resources/dir"):
        os.mkdir("./resources/dir")
        for i in range(0, 3):
            with open(f"./resources/dir/test-{i}.txt", "w") as file:
                file.write('This is for testing')

def remove_entries():
    pass

@patch('builtins.input', side_effect=['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'])
def test_delete_01(mock_input):
    create_test_dir()
    clean("./resources", ["-s"])
    assert os.path.exists("./resources")

@patch('builtins.input', side_effect=['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'])
def test_delete_02(mock_input):
    create_test_dir()
    clean("./resources", ["-s"])
    assert len(os.listdir("./resources")) == 0

@patch('builtins.input', side_effect=['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'])
def test_delete_03(mock_input):
    create_test_dir()
    clean("./resources", ["-s"])
    assert len(os.listdir("./resources")) == 4 and len(os.listdir('./resources/dir')) == 3

@patch('builtins.input', side_effect=['yes', 'yea', 'y', 'yup', 'yep', 'yeah', 'okeydokey', 'aye'])
def test_delete_04(mock_input):
    create_test_dir()
    clean("./resources", ["-s"])
    assert os.path.exists("./resources") and len(os.listdir("./resources")) == 0

@patch('builtins.input', side_effect=['uh-huh', 'yes', 'duh', 'y', 'uh-huh', 'duh', 'uh-huh', 'duh', 'uh-huh', 'duh'])
def test_delete_05(mock_input):
    create_test_dir()
    clean("./resources", ["-s"])
    assert os.path.exists("./resources") and len(os.listdir("./resources")) == 0

