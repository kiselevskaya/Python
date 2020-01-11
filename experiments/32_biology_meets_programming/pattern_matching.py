

v = open('vibrio_cholerae_genome.txt', 'r')
cholerae = v.readlines()[0]
v.close()

t = open('thermotoga_petrophila_genome.txt', 'r')
petrophila = t.readlines()[0]
t.close()


def pattern_matching(pattern, genome):
    positions = []   # output variable
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions


# print(pattern_matching("CTTGATCAT", genome))
# print(pattern_matching("ATGATCAAG", genome))  # [116556, 149355, 151913, 152013, 152394, 186189, 194276, 200076, 224527, 307692, 479770, 610980, 653338, 679985, 768828, 878903, 985368]
# print(len(pattern_matching("ATGATCAAG", genome)))   # 17
