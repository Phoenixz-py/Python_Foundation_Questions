count = 0

with open(r"toread.txt", "r") as nl:
   data = nl.read()
   lines = data.split()
   count += len(lines)

print(count)