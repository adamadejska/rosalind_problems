###################################################################
# Hamming Distance Problem
###################################################################

# Given two DNA strings.
# return an integer value representing the Hamming distance.

with open("rosalind_ba1g.txt", 'r') as f:
    t1 = f.readline().strip()
    t2 = f.readline().strip()

def Hamming_distance(t1, t2):
    dist = 0
    for i in range(0, len(t1)):
        if t1[i] != t2[i]:
            dist = dist+1

    return dist

print(Hamming_distance(t1, t2))