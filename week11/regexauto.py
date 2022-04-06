import re
fname = input("Enter file name: ")
fh = open(fname)
total = 0
for line in fh:
    numlst = list()
    nums = re.findall('[0-9]+', line)
    #print(nums)
    for num in nums:
        intnum = int(num)
        numlst.append(intnum)
    total = total + sum(numlst)
print(total)
