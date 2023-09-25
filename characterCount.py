
#Description
#"Write a function that takes a string as input and returns each character and its count in alphabetical order."

def characterCount(word):
    charCount = {}
    for char in word:
        if char.isalpha():
            char = char.lower()
            if char in charCount:
                charCount[char] +=1
            else:
                charCount[char]=1
    sortedChar=sorted(charCount.keys())
    result= ' '
    for char in sortedChar:
        result +=char+str(charCount[char])
    return result
word = "Hellow"
result = characterCount(word)
print(result)