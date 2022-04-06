fhand = open('mbox-short.txt')
hours= dict()

for line in fhand:
    words = line.split()

    if len(words) < 5 or words[0] != 'From'  : continue
    word = words[5]
    #print(word)
    hr = word.split(":")
    #print(hr)

    if hr[0] not in hours:
        hours[hr[0]] = 1

    else:
        hours[hr[0]] += 1
        #print(hours)

newlst = sorted(hours.items())
for k,v in newlst:
    print(k,v)







#print(newlst)

#print(sorted(hours))

#print(hours)
