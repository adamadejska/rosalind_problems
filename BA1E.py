###################################################################
# Find patterns forming clumps in a string.
###################################################################

# Given a string Genome, and integers k, L, and t.
# return  all distinct k-mers forming (L, t)-clumps in Genome.

def PatternCount(Text, Pattern, t):
# Function from problem BA1A for counting patterns in a text string
    count = 0
    for i in range(0, len(Text) - len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1

    if count >= t:
        return Pattern
    else:
        return 0

def FrequentWords(Text, k, t):
    # Count all occurences of all k-mers found in Text
    tried = []
    solution = []
    for i in range(0, len(Text)-k):
        p = Text[i:i+k]
        if p not in tried:
            tmp_result = PatternCount(Text, p, t)
            tried.append(p)

            if tmp_result != 0:
                solution.append(tmp_result)

    return solution

with open("rosalind_ba1e.txt", 'r') as f:
    Genome = f.readline().strip()
    numbers = f.readline().strip().split(" ")

k = int(numbers[0])
l = int(numbers[1])
t = int(numbers[2])

main_solution = []

for j in range(0, len(Genome)-l):
    Text = Genome[j:j+l]
    main_solution += (FrequentWords(Text, k, t))

main_solution = list(set(main_solution))
print(' '.join(main_solution))