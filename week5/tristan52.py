#assignment 5.1
#Tristan Werden
#TODO: None
#NOTES: Rather than a while True statement here, a do while would have looked a lot better.


num = 0
count = 0
min = None
max = None

while True :
    num = input("Enter Number: ")
    if num == "done" :
        break

    try :
        testnum = int(num)


        if count == 0 :
            min = testnum
            max = testnum

        count = count + 1

        if min >= testnum :
            min = testnum
        if max <= testnum :
            max = testnum

    except :
        print("Invalid input")
        continue




print("Maximum is", max)
print("Minimum is", min)
