name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hours = dict()

for line in handle:
    words = line.split()
    if len(words) < 5 or words[0] != 'From' :
        continue
    word = words[5]
    hr = word.split(':')
    if hr[0] not in hours:
        hours[hr[0]] = 1
    else:
        hours[hr[0]] += 1
newlst = sorted(hours.items())
for k, v in newlst:
    print(k, v)
