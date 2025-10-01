###################################################################
# Find the Most Frequent Words in a String
###################################################################

# Patter is a most frequent k-mer in Text if it maximizes Count(Text,Pattern)
# among all k-mers
# Given a DNA string Text and an integer k
# Return all most frequent k-mers in text separated by space


def PatternCount(Text, Pattern):
# Function from problem BA1A for counting patterns in a text string
    count = 0
    for i in range(0, len(Text) - len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

bases = ['A', 'T', 'C', 'G']

# Read in the variables
with open("rosalind_ba1b.txt", 'r') as f:
    Text = f.readline().strip()
    k = int(f.readline().strip())

# Count all occurences of all k-mers found in Text
string_count = {}
for i in range(0, len(Text)-k):
    p = Text[i:i+k]
    if p not in string_count.keys():
        string_count[p] = PatternCount(Text, p)


# Find the maximum value in the dictionary
max_value = max(string_count.values())

# Use list comprehension to find all keys associated with this maximum value
keys_with_max_value = [key for key, value in string_count.items() if value == max_value]

print(' '.join(keys_with_max_value))