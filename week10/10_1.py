text = dict()

fhand = open('words.txt')

for line in fhand:
    words = line.split()
    for word in words:
        text[word.lower()] = 1
ask = input('What word are you looking for? ')

if ask.lower() in text:
    print('Yes it is!')
else:
    print("No it isn't")
