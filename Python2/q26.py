import random

fileName = "toread.txt"

with open(fileName, "r") as fileContent:
    file_lines = fileContent.read().splitlines()

    print(random.choice(file_lines))