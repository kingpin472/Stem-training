#funtion to replace characters in strings
def replace_in(phrase):
    word=""
    for letter in phrase:
        if letter.lower() in "a,e,i,o,u":
            word=word +"g"
        else:
            word=word+letter
    return word
print(replace_in(input("enter phrase  ")))            





