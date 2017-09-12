# Steven Kundert
# CMPS 5323 - Simpson
# HW 2 - Restriction Enzymes
# 9/13/17
#
#
#

# Take a DNA sequence, return a list of substrings
def HaeIII(dna):
	lst = []
	str1 = 'GGCC'
	start = 0
	while start != len(dna) - 1:
		end = dna.find(str1, start) + 2
		if end > len(dna):
			end = len(dna) - 1
		lst.append(dna[start:end])
		start = end
	return lst
		
		
	
sequence = 'ACGAACATCTTTGGCCAACTAGACCTGGCCAACCTAGCGG'	
subseqs = HaeIII(sequence)
intab = 'ACGT'
outtab = 'TGCA'
trantab = str.maketrans(intab, outtab)
for i in subseqs:
	print(subseqs[i], '\n')
	print(subseqs[i].translate(trantab), "\n\n")
