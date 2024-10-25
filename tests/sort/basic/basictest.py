import os.path
from clean import clean
from organize import sort
import pytest

def init_resources():
    files = ["image.png", "sound.mp3", "file.txt", "program.sh", "book.epub", "data.csv", "schema.sql", "resume.docx", "fish.mp4", "test.zip"]

    if not os.path.exists("./resources"):
       os.mkdir("./resources")
    clean("./resources", [])
    for i in range(0, 10):
        with open(f"./resources/{files[i]}", "w") as file:
            pass
    os.mkdir("./resources/resume")
    for i in range(0, 2):
        with open(f"./resources/resume/resume_0{i}.docx", "w"):
            pass
    os.mkdir("./resources/dir")
    for i in range(0, 10):
        with open(f"./resources/dir/{files[i]}", "w"):
            pass

def test_sort_01():
    init_resources()
    sort("./resources", "-b")
    assert os.path.exists("./resources") and len(os.listdir("./resources")) == 11

def test_sort_02():
    init_resources()
    sort("./resources", "-b")
    assert os.path.exists("./resources/images")
    assert os.path.exists("./resources/audio")
    assert os.path.exists("./resources/text")
    assert os.path.exists("./resources/programs")
    assert os.path.exists("./resources/ebook")
    assert os.path.exists("./resources/tables")
    assert os.path.exists("./resources/databases")
    assert os.path.exists("./resources/videos")
    assert os.path.exists("./resources/archives")

def test_sort_03():
    init_resources()
    sort("./resources", "-b")
    assert os.path.exists("./resources/resume") and len(os.listdir("./resources/resume")) == 3

def test_sort_04():
    init_resources()
    sort("./resources", ["-b", "-r", "uplift"])
    assert not os.path.exists("./resources/dir")