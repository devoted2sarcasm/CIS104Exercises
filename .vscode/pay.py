#calculating gross pay to include overtime, terminating with non-numeric input
hours = input("Total hours: ")
ot = input("Overtime hours: ")

try:
    fh = float(hours)
    fot = float(ot)
    rate = input("Enter pay rate: ")
    try:
        fr = float(rate)
        if fot > 0 :
            reg = fh - fot
            base = reg * fr
            otpay = fot * (fr * 1.5)
            gross = base + otpay
        else :
            gross = fh * fr
        print(f"Pay: {gross:.2f}")
    except:
        print("please enter numbers")
except:
    print("please enter numbers")
