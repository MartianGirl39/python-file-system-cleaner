import pytest
import os
from clean import clean


def create_test_dir():
    file_names = ["cat", "dog", "bunny", "racoon-dog", "tiger", "pig", "doggo", "sheep", "big-dog-big"]
    if os.path.exists("./resources"):
        clean("./resources", [])
    else:
        os.mkdir("./resources")
    for i in range(0, 9):
        with open(f"./resources/{file_names[i]}.txt", "w") as file:
            file.write('This is for testing')
    if not os.path.exists("./resources/dir"):
        os.mkdir("./resources/dir")
    if not os.path.exists("./resources/dogs"):
        os.mkdir("./resources/dogs")

def test_delete_01():
    create_test_dir()
    clean("./resources", ["-p", "dog"])
    assert os.path.exists("./resources")

def test_delete_02():
    create_test_dir()
    deleted = clean("./resources", ["-p", "dog"])
    count = 0
    with os.scandir('./resources') as entries:
        for entry in entries:
            count += 1
    assert count == 6

def test_delete_03():
    create_test_dir()
    clean("./resources", ["-p", "dog"])
    assert os.path.exists("./resources/dir")

def test_delete_04():
    create_test_dir()
    clean("./resources", ["-p", "dog"])
    assert not os.path.exists("./resources/dogs")