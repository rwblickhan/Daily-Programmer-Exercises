#Reverse a String
#Given a string, returns the reverse of the string.
def reverseString(str):
    newStr = ''
    i = len(str) - 1
    while i >= 0:
        newStr = newStr + str[i]
        i = i - 1
    return newStr

print reverseString("Hello")
print reverseString("Cats")
print reverseString("m")
print reverseString("    ")
print reverseString("hELLO")
