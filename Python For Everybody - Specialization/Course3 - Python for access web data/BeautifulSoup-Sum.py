#Scraping Numbers from HTML using BeautifulSoup
 
#In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1030505.html (Sum ends with 44)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import ssl

ctx= ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter-")
html=urllib.request.urlopen(url, context=ctx).read()

Soup = BeautifulSoup(html,'html.parser')

count_of_spans = 0
sum = 0

spans = soup('span')
for span in spans:
    sum += int(span.contents[0])
    count_of_spans += 1

print('Count ', count_of_spans)
print('Sum ', sum)
