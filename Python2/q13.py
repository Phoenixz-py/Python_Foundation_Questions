import linecache


import linecache

a = int(input('Enter how many lines you want to read fron start: '))
line = linecache.getline(r"C:\Users\Yash\IdeaProjects\assignment2\toread.txt", a)

print(line)