"""
Steven Kundert
Bioinformatics - Simpson
Biopython Homework
Created on Mon Nov 13 00:30:04 2017
"""
#1
from Bio import SeqIO

#2
records = SeqIO.read('mycoplasma.gb', 'genbank')

#3, 4, 5
print('ID:', records.id)
print('Description:', records.description)
print('Number of Features:', len(records.features))

#Accumulators needed for step 6
numtRNA = 0
numGenes = 0
numCDSfeatures = 0

#6 loop thru the features counting the number of tRNA, gene, and CDS features
for item in records.features:
    if item.type == 'tRNA':
        numtRNA += 1
    elif item.type == 'gene':
        numGenes += 1
    elif item.type == 'CDS':
        numCDSfeatures += 1
        
#7, 8, 9        
print("\nNumber of tRNA's:", numtRNA)
print('Number of genes:', numGenes)
print('Number of CDS features:', numCDSfeatures)

#10
print('\nThe following feature is feature 4')
print(records.features[4])

#11 thru 15
print('\nThe following information is about feature 21')
print('It is a', records.features[21].type, 'feature')
print('Its location is', records.features[21].location)
print('It is using the translation table', records.features[21].qualifiers['transl_table'])
first20p = str(records.features[21].qualifiers['translation'])
print('The first 20 characters of its sequence are', first20p[2:22])
first50n = str(records.seq)
print('And finally the first 50 nucleotides of the entire sequence are')
print(first50n[:50])