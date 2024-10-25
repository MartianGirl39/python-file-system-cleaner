import pytest
import os

@pytest.fixture
def create_test_dir():
    os.mkdir("./resources")
    for i in range(0, 9):
        with open(f"./resources/test{i}.txt", "w") as file:
            file.write('This is for testing')
    os.mkdir(("./resources/dir"))
    for i in range(0, 9):
        with open(f"./resources/dir/embedded-dir-test{i}.txt", "w") as file:
            file.write('This is for testing')

