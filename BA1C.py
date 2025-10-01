###################################################################
# Find the Reverse Complement of a String
###################################################################

# Given a string of DNA Pattern
# Return a reverse complement of Pattern

with open("rosalind_ba1c.txt", 'r') as f:
    Pattern = f.readline().strip()

complements = {'A' : 'T', 'T': 'A', 'C':'G', 'G':'C'}
rev_complement = ''.join([complements[i] for i in Pattern][::-1])
print(rev_complement)