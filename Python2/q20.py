with open(r"toread.txt", "r") as fl:
    lines = len(fl.readlines())
    print("Total numbers of lines in the text is", lines)
