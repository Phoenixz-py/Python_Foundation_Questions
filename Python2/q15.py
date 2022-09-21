print('Enter value in -')
a = int(input('Enter how many lines you want to read fron start: '))

with open("toread.txt") as f:
    last_n_lines = f.readline()[-a:]

print(last_n_lines)

