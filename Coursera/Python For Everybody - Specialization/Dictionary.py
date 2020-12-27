#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#open and reads the file
fname = input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
handle = open(fname) 

#list for storing words 
lst = list()

for line in handle:
    if not line.startswith("From:"): continue
    #string split method for chopping the string in to words
    line = line.split()
    #adding each words in to empty list that we have created before. using append method. 
    lst.append(line[1])

#create dictionary for storing total counts
counts = dict()
for word in lst:
    #appending counts to the dictionary using get method. 
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
#resultant key-value pair is needed for the final output. and for that items method is useful. 
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)


#this code contains file operation, String operation, dictionary(for count) and list for storing words. So the best example to understand the use of file and collection data structures. 
