text = dict()
maxsend = None
maxcount = None

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

for line in handle:
    words = line.split()
    if len(words) < 1 or words[0] != 'From' :
        continue
    text[words[1]] = text.get(words[1], 0) + 1
for word,count in text.items() :
    if maxcount is None or count > maxcount :
        maxsend = word
        maxcount = count

print(maxsend,maxcount)
