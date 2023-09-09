# count file numbers
import os

dir_list = [
    "demo",
    "easy",
    "hard",
    "medium",
    "test",
    "playground",
]

for dir in dir_list:
    file_count = 0
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".py") or file.endswith(".ipynb"):
                file_count += 1
    print(f"{dir}: {file_count}")