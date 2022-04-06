import re
usercheck = input("Enter a regular expression: ")
fname = "mbox.txt"
fh = open(fname)
count = 0

for line in fh:
    if re.search(usercheck, line):
        count += 1
    else:
        continue

print(f"{fname} had {count} lines that matched {usercheck}")
