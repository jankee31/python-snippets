#Extracting data with regular expressions


import re
file=input("Enter file name:")
if len(file)<1:
 name="Actual.txt"
handle=open(file)
newlist=list()
for line in handle:
 line=re.findall('[0-9]+',line)
 for number in line:
  newlist.append(int(number))
print(sum(newlist))
