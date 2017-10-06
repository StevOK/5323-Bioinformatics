# Steven Kundert
# CMPS 5323 - Bioinformatics - Simpson
# Project 3 parts A, B and C - Open Reading Frames

# In part A, this program reads a complete DNA sequence from a FASTA file and stores
# it as a string. It then does a triple pass on that string and its complement
# to find all start and stop codons in each frame, as well as the number of
# large stop blocks of 600 or more characters between stop codons. The stops
# and associated starts are stored in dictionaries.

# In part B, this program reads a GenBank file that corresponds to the DNA sequence
# and scrapes from it a list of all the genes that have been found in both the
# DNA and its complement. It then looks for both the shortest and longest
# genes found in the GenBank file, as well as the number of genes found.

# In part C, the program matches the genes found in the GenBank file against
# the dictionaries containing the stops and associated stops found in the DNA
# strand and its complement. It finds the five longest genes matched this way,
# and displays whether that gene is in the original DNA sequence or its complement.
# The number of matches and number of misses are also displayed.

import re

# Part A

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

# Create dictionaries to associate each stop codon with the start codons that precede it
stopandstartsdict = dict()
compsandsdict = dict()

# For part C, need to total number of large stop blocks
totallargeblocks = 0

print('Original DNA Sequence Analysis:')

# Pass through each frame of the original DNA sequence
for frame in range(3):
    startlist = []
    numstarts = 0
    numstops = 0
    largestops = 0
    laststop = 0
    # For each codon in the frame
    for i in range(0,len(dna),3):
        # Look for start codons and incrememnt when one is found
        # Then put the start codon in the current list of starts 
        if(dna[i+frame:i+frame+3]==startcodon):
            numstarts = numstarts + 1
            startlist.append(i+frame)           
        # Otherwise look for stop codons
        elif(dna[i+frame:i+frame+3] in stopcodons):
            numstops = numstops + 1             # Increment when a stop codon is found
            # Associate the list of most recents start codons with the stop codon
            # Then clear the list of start codons
            stopandstartsdict[(i+frame)] = startlist
            startlist = []
			# If the distance between the current and previous stop codons is 600 or more
            if((i+frame - laststop) >= 600 and laststop > 0):     
                largestops = largestops + 1     # Increment number of large stop blocks found
            laststop = i+frame                  # Then update the location of the most recent stop
    # Update the running total of large stop blocks
    totallargeblocks = totallargeblocks + largestops
    # Print specified information for each frame
    print('Frame #:',frame,', startct =',numstarts,', stopct =',numstops,', large stop blocks =',largestops)
    
    
print('\nReversed Complementary DNA Sequence Analysis:')
# Perform the same triple pass of the orginal DNA sequence's complement
for frame in range(3):
    startlist = []
    numstarts = 0
    numstops = 0
    largestops = 0
    laststop = 0
    for i in range(0,len(complement),3):
        if(complement[i+frame:i+frame+3]==startcodon):
            numstarts = numstarts + 1
            startlist.append(i+frame)
        elif(complement[i+frame:i+frame+3] in stopcodons):
            numstops = numstops + 1
            compsandsdict[(i+frame)] = startlist
            startlist = []
            if((i+frame - laststop) >= 600 and laststop > 0):
                largestops = largestops + 1
            laststop = i+frame
    totallargeblocks = totallargeblocks + largestops
    print('Frame #:',frame,', startct =',numstarts,', stopct =',numstops,', large stop blocks =',largestops)
    
# Part B

# Create lists to hold the beginning and end of each gene in both the original
#  DNA strand and its complement   
genelist = []
compgenelist = []    

# Compile the regular expressions we will use
gene = re.compile('^CDS ')      # Had to use CDS instead of gene because of tRNA
com = re.compile('complement')
num = re.compile('[0-9]+')

# Open the Gen Bank file
gbfile = open('sequence.gb', 'r')

# For each line of the Gen Bank file
for lines in gbfile:
    lines = lines.strip()           # Strip the whitespace from the left and right side of the line
    # Find each line designated as a gene
    if re.search(gene, lines):    
        # If the gene is a complement add the list of the two numbers to the list of all
        #  genes in the DNA's complement
        if re.search(com, lines):   
            compgenelist.append(re.findall(num, lines))
        # Otherwise add the list of the two numbers to the list of all the genes
        #  in the original DNA strand
        else:
            genelist.append(re.findall(num, lines))

# Edit the lists so that they are int instead of string, then offset them so
#  they match the dictionaries of associated stop and start codons
for item in genelist:
    item[0] = int(item[0]) - 1
    item[1] = int(item[1]) - 3
for item in compgenelist:
    item[0] = int(item[0])
    item[1] = int(item[1])
    # Since the numbers in the list of genes in the DNA's complement are the
    #  indices used in the original DNA strand, we must convert them to their
    #  positions in the complement, including a swap so that the two numbers
    #  are in ascending order
    temp = len(complement) - item[0]
    item[0] = len(complement) - item[1]
    item[1] = temp - 2
    
# Initialize variables for the longest and shortest genes, 
#  as well as the number of genes in the two lists
longestgene = 0
shortestgene = len(dna)
numgenes = 0

# Process the list of genes in the original DNA strand
for genes in genelist:
    numgenes = numgenes + 1                 # Increment number of genes in list
    if (genes[1]-genes[0]) > longestgene:   # Finds the longest gene
        longestgene = genes[1] - genes[0]
    if (genes[1]-genes[0] < shortestgene):  # Finds the smallest gene
        shortestgene = genes[1] - genes[0]
        
# Process the list of genes in the DNA's complement
for genes in compgenelist:
    numgenes = numgenes + 1
    if (genes[1]-genes[0]) > longestgene:
        longestgene = genes[1] - genes[0]
    if (genes[1]-genes[0] < shortestgene):
        shortestgene = genes[1] - genes[0]
        
print('\nGenBank File Analysis:')
print('Smallest gene:',shortestgene,'nucleotides, Longest gene:',longestgene,'nucleotides, Number of genes:', numgenes)

# Part C  

# Create a list of all the genes found in both of the lists of genes and both
#  dictionaries, as well as the number of them found
foundlist = []
numfound = 0 

# Match the genes listed in the GenBank file to the dict of large stop blocks
#  in the DNA strand 
for keys in genelist:
    # Check if the end of the gene is in the list of stops
    if keys[1] in stopandstartsdict:
        # Check to see if the beginning matches a start associated with the stop
        if keys[0] in stopandstartsdict[keys[1]]:
            numfound = numfound + 1
            # Put the start, stop, size and strand in a list of lists
            foundlist.append([keys[0],keys[1],keys[1]-keys[0], 'original strand'])
    
# Match the complementary genes listed in the GenBank file with the dict of
#  large stop blocks in the complementary strand
for keys in compgenelist:
    if keys[1] in compsandsdict:
        if keys[0] in compsandsdict[keys[1]]:
             numfound = numfound + 1
             foundlist.append([keys[0],keys[1],keys[1]-keys[0], 'complementary strand'])
     
# Sort the list of matches by length of gene in descending order        
foundlist.sort(key=lambda x:x[2], reverse=True)

print('\nNumber of Genes Located in Both Files:',numfound)
print('Largest Genes Matched:')
for j in range(0,5):
    print('From',foundlist[j][0],'to',foundlist[j][1]+3,'in',foundlist[j][3])
print('Large Open Reading Frames not Matched to GenBank File:', totallargeblocks - numfound)