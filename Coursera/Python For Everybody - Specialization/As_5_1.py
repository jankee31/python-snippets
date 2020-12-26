#write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the TOTAL, COUNT and AVERAGE of the numbers. If the user enteres anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
 
num=0
tot=0.0
while True:
	sval=input("Enter a number:")
	if sval=='Done':
		break
	try:
		fval=float(sval)
	except:
		print('Invalid Input')
		continue
	num=num+1
	tot=tot+fval
print(tot,num,tot/num)
