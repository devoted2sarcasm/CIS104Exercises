#just to establish how much we're actually tipping for final calculation of actual bills
def tip():
    while True:
        tip = input("How much would you like to tip? (15/18/20)")
        try:
            itip = int(tip)
        except:
            print(f"I'm sorry, {tip} doesn't look like good input, try typing just '15', '18', or '20'")
            continue
        return itip
        break

#defining how many bills we'll need, assuming even split
def split():
    maybe = input("Would you like the bill split? (y/n)")
    while True:
        if maybe == "y":
            split = input("Into how many bills?")
            try:
                isplit = int(split)
            except:
                print("I'm sorry, that doesn't seem to work for me, try again?")
                continue
            return isplit
            break
        elif maybe == "n":
            isplit = 1
            return isplit
            break
        elif maybe != "y" and maybe != "n":
            print("I'm sorry, I was looking for a 'y' or 'n', please try again")
            continue


while True:
    bill = input("How much was your bill? ")
    try:
        ibill = float(bill)
    except:
        print("I'm sorry, that doesn't seem like number I can work with, let's try that again.")
        continue
    break
bill15 = ibill * 0.15
bill18 = ibill * 0.18
bill20 = ibill * 0.20
t15 = round((ibill + bill15), 2)
t18 = round((ibill + bill18), 2)
t20 = round((ibill + bill20), 2)
print("Suggested tip allotments:")
print(f"15% = {bill15:.2f}, total bill = {t15:.2f}")
print(f"18% = {bill18:.2f}, total bill = {t18:.2f}")
print(f"20% = {bill20:.2f}, total bill = {t20:.2f}")

itip = tip()

each = split()

if each > 1:
    print(f"Your total bill for {each} persons with {itip} percent tip is:")
    if itip == 15:
        print(round(float(t15/each), 2))
    elif itip == 18:
        print(round(float(t18/each), 2))
    elif itip == 20:
        print(round(float(t20/each), 2))
else:
    print(f"Your total bill was calculated above for {itip}% tip, please refer to that and have a great day!")
