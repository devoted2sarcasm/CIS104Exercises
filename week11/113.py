fhand = input("Enter a File Name:")
fh = open(fhand)
letters_lst = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter in alphabet:
    letters_lst[letter] = letters_lst.get(letter,0)
#print(letters_lst)


for line in fh:
    words = line.split()
    for word in words:
        letters = list(word)
        for letter in letters:
            if letter in letters_lst:
                letters_lst[letter] += 1
#print(letters_lst)

output = list()
for k,v in letters_lst.items():
    output.append((v,k))

output = sorted(output, reverse=True)

for k,v in output:
    print(v,k)
