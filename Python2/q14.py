import linecache

divine = open("toread.txt", "a")

divine.write("Appending a line as txt to the file")

divine.close

reado = linecache.getline(r"C:\Users\Yash\IdeaProjects\assignment2\toread.txt", 4)

print(reado)