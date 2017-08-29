#Steven Kundert
#CMPS 5323 - Bioinformatics - Simpson
#Fibonacci Warmup
#8/29/2017
#This program creates a list, then fills it with the first 5000
# numbers in the Fibonacci Sequence, iteratively. It then reads
# a file of numbers and prints each number's corresponding 
# Fibonacci number.

fib = [0, 1]

for n in range(2, 5000):
	fib.append(fib[n-1] + fib[n-2])
	
file = open('fibdata.txt', 'r')
line = file.readline()
while line:
	k = int(line)
	print('The Fibonacci number for', k, 'is', fib[k])
	line = file.readline()
