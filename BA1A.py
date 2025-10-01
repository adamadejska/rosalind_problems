###################################################################
# Compute the Number of Times a Pattern Appears in a Text
###################################################################

# A k-mer is a string of length k.
# Count(Text, Pattern) is a function that counts how many
# times k-mer Paterrn appears as a substring of Text.
# It accounts for overlapping occurences of Pattern in Text.

def PatternCount(Text, Pattern):
    count = 0
    for i in range(0, len(Text) - len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

with open("rosalind_ba1a.txt", 'r') as f:
    t = f.readline().strip()
    p = f.readline().strip()

print(PatternCount(t,p))