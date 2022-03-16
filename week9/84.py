fname = input("Enter file name: ")
fhand = open(fname)
all = list()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in all:
            all.append(word)
all.sort()
print(all)
