fhand = open('mbox-short.txt')
email_adresses = dict()  #create a blank dictionary

for line in fhand:
    words = line.split()    #creates a list of words on line

    if len(words) < 3 or words[0] != 'From'  : continue  #filter line for minimum words and From as first word

    if words[1] not in email_adresses:
        email_adresses[words[1]] = 1
    else:
        email_adresses[words[1]] += 1
#lines 9-13 either establish an initial count or add one to previous count
#print(email_adresses)

email_lst = list()  #16-18 create an empty list and populates it with the dictionary items
for k,v in email_adresses.items():
    email_lst.append((v,k))

email_lst = sorted(email_lst, reverse=True)

for k,v in email_lst[:1]:
    print(v,k)
