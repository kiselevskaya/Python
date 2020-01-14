
from pattern_count import *


e = open('e.coli.txt', 'r')
e_coli = e.readlines()[0]
e.close()


def symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2]
    for i in range(n):
        array[i] = pattern_count(extended_genome[i:i+(n//2)], symbol)
    return array


def faster_symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2]
    # look at the first half of Genome to compute first array value
    array[0] = pattern_count(genome[0:n//2], symbol)
    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if extended_genome[i-1] == symbol:
            array[i] = array[i]-1
        if extended_genome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


def skew_array(genome):
    skew = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2]
    skew[0] = 0
    for i in range(1, n+1):
        skew[i] = skew[i-1]
        if extended_genome[i-1] == "G":
            skew[i] = skew[i-1]+1
        if extended_genome[i-1] == "C":
            skew[i] = skew[i-1]-1
    return list(skew.values())


def minimum_skew(genome):
    positions = []
    skew = skew_array(genome)
    lowest = min(skew)
    for i in range(len(skew)):
        if skew[i] == lowest:
            positions.append(i)
    return positions


# print(symbol_array(e_coli, "C"))
# print(faster_symbol_array(e_coli, "C"))
print(skew_array("CATGGGCATCGGCCATACGCC"))
# print(skew_array("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"))
# print(minimum_skew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"))
