#Ken Page
#CIS104 - Winter 2022
#Midterm - q4

#counting function, should count by 2 unless number is only 1 more, print every time it counts a new number, returning final number
def counting(number, counter):
    while counter < number :
        if counter + 1 == number :
            counter = counter + 1
            print(counter)
            continue
        else :
            counter = counter + 2
            print(counter)
            continue
        return counter

#taking user input for number to count to
num = input("Enter a number to count to: ")

#error-checking for number as input
try:
    inum = int(num)
    count = 0
    counting(inum, count)
except:
    print("Sorry, that doesn't look like a number I can work with, please try again")

#fin
print("Thanks for using the counting program!")
