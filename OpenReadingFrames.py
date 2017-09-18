# Steven Kundert



# Save FASTA file

# Open Fasta for reading

# read in fasta file as one long string

# there are many more start codons than stop codons
# never ignore a stop
# starts don't gaurantee the actual start of a gene
# perhaps many starts inside a gene

# upstream from the real start there may be a promoter 
# TAATAA box, TATA boxes / motif

# count starts and stops
# genes are 'conserved' - very few changes over time



# Traverse sequence
# ORF_Dict = Dict()
# Every time you see a start, add it to a list
# startlist = []
# startlist.append(pos)

# if stop codon found & startlist is empty
# orf-dict[stop-pos] = startlist # til find stop?
# startlist = []

#maybe pair list of starts with position of stop in a dict
# compare each dict against each gene start and stop in the file

#got to write a program to strip each gene start and stop pos
# find all genes, get the two numbers
# some genes have complement() surrounding numbers

#look up pattern matching / reg ex: DTU bioinformatics pattern matching