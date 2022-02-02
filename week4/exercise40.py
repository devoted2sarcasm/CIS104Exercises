def calc():
    n1 = input("Please enter a number:")
    n2 = input("Please enter another number:")
    n3 = input("Please enter one more number:")
    high = max(n1, n2, n3)
    return high

print("Let's do some numbers")
call1 = calc()
print("The highest number you entered was", call1)
print("Let's do that again")
call2 = calc()
print("The highest number you entered this time was", call2)
print("One last time...")
call3 = calc()
highest = max(call1, call2, call3)
print("The highest number you entered was", call3, "but the highest you entered through all of these was", highest)
print("Thanks for playing")
quit()
