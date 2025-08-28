with open("rosalind_ini3.txt", 'r') as f:
    text = f.readline()
    a,b,c,d = f.readline().split()
    a,b,c,d = int(a), int(b), int(c), int(d)

print(text[a:b+1] + ' ' + text[c:d+1])