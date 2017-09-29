#Steven Kundert
#CMPS 5323 - Bioinformatics - Simpson
#Fibonacci Warmup
#8/29/2017
#This program creates a list, then fills it with the first 5000
# numbers in the Fibonacci Sequence, iteratively. It then reads
# a file of numbers and prints each number's corresponding 
# Fibonacci number.

#Create list, fill in its first two entries
fib = [0, 1]

#Generate rest of list
for n in range(2, 5001):
	fib.append(fib[n-1] + fib[n-2])
	
#Open input file for reading	
file = open('fibdata.txt', 'r')

#Read the first line
line = file.readline()

#While there are still lines in the input file
while line:
	#Convert each line into an integer
	k = int(line)
	#Print the number and its corresponding Fib number
	print('The Fibonacci number for', k, 'is', fib[k])
	#Read in the next line
	line = file.readline()
