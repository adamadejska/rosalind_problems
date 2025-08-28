from collections import Counter

with open("rosalind_ini6.txt", 'r') as f:
    text = f.readline().strip().split()

d = Counter(text)
for k,v in d.items():
    print(k + ' ' + str(v))