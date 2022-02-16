#assignment 5.1
#Tristan Werden
#TODO: None
#NOTES: Rather than a while True statement here, a do while would have looked a lot better.

num = 0
avg = 0
count = 0
total = 0

while True :
    num = input("Enter Number: ")
    if num == "done" :
        break

    try :
        float(num)
        print("GARBAGE")
        count = float(count) + 1
        total = float(total) + float(num)
        avg = float(total) / float(count)
    except :
        print("Error, please enter numeric input")
        continue


print(total, count, avg)
