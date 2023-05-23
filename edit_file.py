#this  is for editing a txt file named alice.txt so that it doesn't contain special characters and all letters are lowercase.
import string

def strip_punc(line):
    for character in string.punctuation:
        #remove characters in string.punctuation
        line = line.replace (character, "")
        words=line.split()
        for word in words:
            #make all words become lowercase
            line=line.replace(word,word.lower())        
    return line

with open ("alice.txt", "r") as alice:
    #creates a list of lines for the file
    lines = alice.readlines()
with open ("alice.txt", "w") as alice:
    for line in lines:
        new_line = strip_punc(line)
        alice.write (new_line)

    
