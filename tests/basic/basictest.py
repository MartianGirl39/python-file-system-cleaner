import pytest
import os
from clean import clean

def create_test_dir():
    if not os.path.exists("./resources"):
        os.mkdir("./resources")
        for i in range(0, 9):
            with open(f"./resources/test{i}.txt", "w") as file:
                file.write('This is for testing')
    if not os.path.exists("./resources/dir"):
        os.mkdir("./resources/dir")
        for i in range(0, 9):
            with open(f"./resources/dir/embedded-dir-test{i}.txt", "w") as file:
                file.write('This is for testing')

def test_delete_01():
    create_test_dir()
    clean("./resources", [])
    assert os.path.exists("./resources") == True

def test_delete_02():
    create_test_dir()
    clean("./resources", [])
    count = 0
    with os.scandir('./resources') as entries:
        for entry in entries:
            count += 1
    assert count == 0

def test_delete_03():
    create_test_dir()
    clean("./resources", [])
    assert os.path.exists("./resources/dir") == False