import re
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    numlst = list()
    nums = re.findall('[0-9]+', line)
    #print(nums)
    for num in nums:
        intnum = int(num)
        numlst.append(intnum)
        count += 1
    total = total + sum(numlst)
    print(numlst, total)
avg = int(total/count)
print(f"Average: {avg}")
