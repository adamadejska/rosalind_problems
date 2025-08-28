import math
with open("rosalind_ini2.txt", 'r') as f:
    for line in f:
        a,b = line.split()

print(int(a)**2 + int(b)**2)