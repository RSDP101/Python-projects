import re
#with open("word_count.txt", "r") as word_count:
#    lines= word_count.readlines()
word_count = open("word_count.txt", "r")
ans =0
for line in word_count:
    y= re.findall("[0-9]+", line)
    for i in y:
        ans=ans+int(i)
print("A soma de todos é", ans)
