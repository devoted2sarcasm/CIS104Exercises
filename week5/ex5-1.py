total = 0
count = 0
avg = 0
while True:
    num = input('Enter a number:')
    if num == 'done':
        break
    try:
        innum = int(num)
    except:
        print('Bad input')
        continue
    total = total + innum
    count = count + 1
    avg = total / count
if count == 0 :
    print('You have provided no numbers for me to calculate, good-bye.')
else :
    print('Total:', total, 'Count:', count, 'Average:', avg)
