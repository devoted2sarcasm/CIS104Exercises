text = dict()

fname = input("Enter file name: ")

fh = open(fname)

for line in fh:
    words = line.split()
    if len(words) < 1 or words[0] != 'From' :
        continue
    address = words[1]
    spltaddress = address.split("@")
    text[spltaddress[1]] = text.get(spltaddress[1], 0) + 1

print(text)
