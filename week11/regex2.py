import re
check = "New Revision"
fname = "mbox.txt"
fh = open(fname)

for line in fh:
    if re.search(check, line):
        print(line)
