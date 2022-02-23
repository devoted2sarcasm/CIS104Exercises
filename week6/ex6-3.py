text = input("Type some stuff:")
findit = input("What letter are you looking for?:")
def count(a, b):
    a = text
    b = findit
    num = 0
    for letter in a:
        if letter == b :
            num = num + 1
    return num

print(count(text, findit))
