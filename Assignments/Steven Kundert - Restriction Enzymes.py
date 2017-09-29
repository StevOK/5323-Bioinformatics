# Steven Kundert
# CMPS 5323 - Simpson
# HW 2 - Restriction Enzymes
# 9/13/17
# This program simulates the cutting up of a DNA strand by the HaeIII 
#  restriction enzyme. A sample DNA sequence is sent into a function
#  where the palindromic subsequence GGCC will be searched for. When
#  the function finds the sequence, it "splits" the strand by creating
#  a new string from the most recent split (or the beginning) to the
#  middle of GGCC. It will continue until the entire strand has been
#  split up and return the list of strings, which are then printed,
#  along with their associated complementary strands.

# Function: HaeIII()
# Input: One string, representing a DNA sequence
# Process: Use the find() method to search for each occurrence of
#			the subsequence GGCC, then append() each subsequence
#			between these endpoints. 
# Output: A list of strings
# Take a DNA sequence, return a list of substrings. This should be 
#  O(n) complexity because of the str.find() calls.
def HaeIII(dna):
    lst = []        	# Create a list to put substrings into
    start = 0       	# Start at the beginning of the string
	endofseq = len(dna)	# Make a value for the end of the line
    
    # While the search hasn't reached the end of the sequence 
    while start < endofseq:
        # Put a splitting point between 'GG' and 'CC'
		# The str.find() call returns -1 if it reaches the end
		#  of the string, so we will get end == 1 then 
        end = dna.find('GGCC', start) + 2
        # If the end of the string has been reached,
        #  put the endpoint at the end of the sequence.
        if end == 1:
            end = endofseq
            
        # Append a substring from the sequence into the list
        lst.append(dna[start:end])
        
        # Put the new start point at the most recent end point
        start = end
       
    return lst
		
# Create a sequence to be cut up
sequence = 'ACGAACATCTTTGGCCAACTAGACCTGGCCAACCTAGCGG'	

# Send sequence to function, store list of strings
subseqs = HaeIII(sequence)

# Create the translation table to mirror each substring
intab = 'ACGT'
outtab = 'TGCA'
trantab = str.maketrans(intab, outtab)

# Print each substring and its complement
for i in subseqs:
	print(i)
	print(i.translate(trantab), "\n")
