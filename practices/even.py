# odd or even program
while True:
    num = input("Enter a number between 1 and 1000:")
    try:
        inum = int(num)
    except:
        print(f'{num} is bad input, try again')
        continue
    if inum > 1000 or inum < 1:
        print(f'{inum} is not between 1 and 1000, please try again')
        continue
    else:
        even = inum
        while even > 2:
            even = even -2
        if even == 2:
            print(f'{inum} is even!')
            quit()
        else:
            print(f'{inum} is odd!')
            quit()
