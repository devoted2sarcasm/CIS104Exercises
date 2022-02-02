#calculating gross pay to include overtime
def computepay():
    if fh > 40.00 :
      ot = fh - 40
      otp = fr * 1.5
      gross = ((fh - ot) * fr) + (ot * otp)
    else : gross = fh * fr
    return gross

hours = input("Enter hours: ")
rate = input("Enter pay rate: ")
fh = float(hours)
fr = float(rate)

print(computepay())
