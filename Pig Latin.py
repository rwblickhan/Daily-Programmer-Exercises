#Pig Latin
#Given a string, returns its "Pig Latin" equivalent.
#That is, it puts the first character at the end and appends 'ay'.
#Note: has not been fixed to correctly de/capitalize characters

def producePigLatin(str):
    if str[0] != 'a' and str[0] != 'e' and str[0] != 'i' and str[0] != 'o' and str[0] != 'u' and str[0] != 'y':
        if str[0] != 'A' and str[0] != 'E' and str[0] != 'I' and str[0] != 'O' and str[0] != 'U' and str[0] != 'Y':
            if len(str) > 1:
                str = str[1:len(str)] + str[0]
    str = str + 'ay'
    return str

print producePigLatin('Apple')
print producePigLatin('Banana')
print producePigLatin('apple')
print producePigLatin('banana')
