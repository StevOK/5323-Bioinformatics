"""
Steven Kundert
Created on Wed Oct 25 00:11:23 2017
"""
# Create a string, this is the example used in the slides
S = 'acacag$'

# Create an empty list to insert each suffix's beginning index into
SA = []

# Put the index for the beginning of the entire string in the list
# A list with one item is sorted
SA.append(0)

# For each suffix of S
for i in range(1, len(S)):
    # Start at the beginning of the list
    j = 0
    # Compare the current suffix with each suffix in the list until
    #  its relative place in the list
    while j < len(SA) and (S[i:] > S[SA[j]]):
        j+=1
    # Insert the item into the list of suffix indexes
    SA.insert(j,i)
    
# Print the suffix array
print (SA)
