###################################################################
# Find All Occurrences of a Pattern in a String
###################################################################

# How many times can one string occur as a substring of another? 
# Given a string Pattern and Genome
# return all starting positions in Genome where Pattern appears as a substring
# using 0-based indexing

with open("rosalind_ba1d.txt", 'r') as f:
    p = f.readline().strip()
    g = f.readline().strip()

indexes = []
for i in range(0, len(g) - len(p) + 1):
    if g[i:i+len(p)] == p:
        indexes.append(str(i))

print(' '.join(indexes))