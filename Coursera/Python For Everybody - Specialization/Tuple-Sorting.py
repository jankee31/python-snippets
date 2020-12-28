#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#"From stephen.marquard@uct.ac.za Sat Jan  5 "09:14":16 2008"
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 :
	 name = "mbox-short.txt"
handle = open(name)

d=dict()
for w in handle:
    if not w.startswith("From "): 
        continue
    else:    
        w=w.split()
        w=w[5]
        w=w[0:2]
        d[w]=d.get(w,0)+1

lst=list()        
for v,k in d.items():
    lst.append((v,k))

lst.sort()
for v,k in lst:
    print (v,k)
