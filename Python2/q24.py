names = ['Jill', 'Cacai', 'Kenken']

with open(r'C:/Users/Yash/IdeaProjects/assignment2/toread.txt', 'w') as fp:
    for item in names:
        fp.write("%s\n" % item)
print("done")