

# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern

def reverse_complement(pattern):
    return complement(reverse(pattern))


def reverse(pattern):
    return pattern[::-1]


def complement(pattern):
    output = []
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for p in pattern:
        output.append(complements[p])
    return ''.join(output)


print(reverse_complement('AAAACCCGGT'))   # ACCGGGTTTT
print(reverse_complement('CCAGATC'))
