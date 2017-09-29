# Steven Kundert
# CMPS 5323 - Bioinformatics - Simpson
# Project 3 part A - Open Reading Frames
# This program reads a complete DNA sequence from a FASTA file and stores
# it as a string. It then does a triple pass on that string and its complement
# to find all start and stop codons in each frame, as well as the number of
# large stop blocks of 600 or more characters between stop codons.


# Create string to concatenate lines to
dna = ""

#Open input file for reading	
file = open('sequence.fasta', 'r')

#Read the first line, then read the second, discarding the header
line = file.readline()
line = file.readline()

# Concatenate each line of the file to the DNA string
while line:
    line = line.replace('\n','')    # Remove all return characters from each line
    dna = dna + line                # Concatenate each line
    line = file.readline()          # Read in the next line
    
# Reverse the DNA sequence
reverse = dna[::-1]

# Make a translation table for DNA
intab = 'ACGT'
outtab = 'TGCA'
trantab = str.maketrans(intab, outtab)

# Translate the reversed sequence into its complement
complement = reverse.translate(trantab) 

# Define start and stop codons
startcodon = 'ATG'
stopcodons = ['TGA','TAG','TAA']

print('Original DNA Sequence Analysis:')

# Pass through each frame of the original DNA sequence
for frame in range(3):
    numstarts = 0
    numstops = 0
    largestops = 0
    laststop = 0
    # For each codon in the frame
    for i in range(0,len(dna),3):
        # Look for start codons and incrememnt when one is found
        if(dna[i+frame:i+frame+3]==startcodon):
            numstarts = numstarts + 1
        # Otherwise look for stop codons
        elif(dna[i+frame:i+frame+3] in stopcodons):
            numstops = numstops + 1             # Increment when a stop codon is found
            # If the distance between the current and previous stop codons is 600 or more
            if(((i+frame - laststop) > 600) and laststop > 0):     
                largestops = largestops + 1     # Increment number of large stop blocks found
            laststop = i+frame                  # Then update the location of the most recent stop
    # Print specified information for each frame
    print('Frame #:',frame,', startct =',numstarts,', stopct =',numstops,', large stop blocks =',largestops)
    
print('\nReversed Complementary DNA Sequence Analysis:')
# Perform the same triple pass of the orginal DNA sequence's complement
for frame in range(3):
    numstarts = 0
    numstops = 0
    largestops = 0
    laststop = 0
    for i in range(0,len(complement),3):
        if(complement[i+frame:i+frame+3]==startcodon):
            numstarts = numstarts + 1
        elif(complement[i+frame:i+frame+3] in stopcodons):
            numstops = numstops + 1
            if((i+frame - laststop) >= 600):
                largestops = largestops + 1
            laststop = i+frame
    print('Frame #:',frame,', startct =',numstarts,', stopct =',numstops,', large stop blocks =',largestops)
