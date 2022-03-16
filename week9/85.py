fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    words = line.split()
    if len(words) < 1 or words[0] != 'From' :
        continue
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
