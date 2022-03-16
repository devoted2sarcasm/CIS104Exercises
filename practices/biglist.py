a = 45
b = 39
c = 32
d = 25
e = 13
list = (a, b, c, d, e)

while True:
    print(f"The list is currently: {list}")
    new = input("Would you like to add a new number?")
    if type(new) is not int:
        print("That doesn't look like a number, so I won't be changing the list. Have a great day!")
        break
    else:
        if new >= a:
            f = e
            e = d
            d = c
            c = b
            b = a
            a = new
            break
        elif new >= b:
            f = e
            e = d
            d = c
            c = b
            b = new
            break
        elif new >= c:
            f = e
            e = d
            d = c
            c = new
            break
        elif new >= d:
            f = e
            e = d
            d = new
            break
        elif new >= e:
            f = e
            e = new
            break
        else:
            print("Oops, something went wrong.")
            break

print(list)
