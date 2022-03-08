word = input("Please type any word you like:")
word = word.lower()
num = len(word)
count = 0
isPalindrome = True
while count < (num/2) :
    if word[count] == word[num-(count+1)] :
        count = count + 1
        continue
    else:
        isPalindrome = False
        break
if isPalindrome == True:
    print("Congrats? That was a palindrome.")
if isPalindrome == False:
    print("That was a great word, but not a palindrome.")
