with open("rosalind_ini4.txt", 'r') as f:
    a,b = f.readline().split()

a,b = int(a), int(b)
s = 0
for i in range(a, b+1):
    if i % 2 == 1:
        s += i

print(s)