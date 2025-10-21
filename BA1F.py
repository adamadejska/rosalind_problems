###################################################################
# Minimum Skew Problem
###################################################################

# Given a DNA string Genome.
# return all integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).

with open("rosalind_ba1f.txt", 'r') as f:
    Genome = f.readline().strip()


skew = [0]
for i in Genome:
    if i == "C":
        skew.append(skew[-1]-1)
    elif i == "G":
        skew.append(skew[-1]+1)
    else:
        skew.append(skew[-1])

minimum = min(skew)
ind = [str(i) for i, val in enumerate(skew) if val == minimum]
print(' '.join(ind))