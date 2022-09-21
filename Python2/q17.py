import linecache

Aru = int(input('Enter how many lines do you want to read: '))
myVar = 0

for i in range(Aru):
    WhatRead = int(input("Which line do you want to read: "))
    Aread = linecache.getline(r"C:\Users\Yash\IdeaProjects\assignment2\toread.txt", WhatRead)
    myVar.append(Aread)

print(myVar)