import re
check = "New Revision"
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0

for line in fh:
    if re.search(check, line):
        revnum = re.findall('[0-9]+', line)
        intrev = int(revnum[0])
        total = total + intrev
        count += 1
avg = int(total/count)
print(f'{check}: {avg}')
        #print(line)
