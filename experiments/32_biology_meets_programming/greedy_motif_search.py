

from score_motifs import profile_matrix, get_score
from probability import profile_most_probable_pattern


def greedy_motif_search(dna, k, t):
    best_motifs = []
    for i in range(0, t):
        best_motifs.append(dna[i][0:k])
    n = len(dna[0])   # 12
    for e in range(n-k+1):
        motifs = []
        motifs.append(dna[0][e:e+k])
        for j in range(1, t):
            prof = profile_matrix(motifs[0:j])
            motifs.append(profile_most_probable_pattern(dna[j], k, prof))
        if get_score(motifs) < get_score(best_motifs):
            best_motifs = motifs
    return best_motifs


k = 3
t = 5
dna = ['GGCGTTCAGGCA', 'AAGAATCAGTCA', 'CAAGGAGTTCGC', 'CACGTCAATCAC', 'CAATAATATTCG']


print(greedy_motif_search(dna, k, t))


dna_for_test1 = ['GAGGCGCACATCATTATCGATAACGATTCGCCGCATTGCC',
                 'TCATCGAATCCGATAACTGACACCTGCTCTGGCACCGCTC',
                 'TCGGCGGTATAGCCAGAAAGCGTAGTGCCAATAATTTCCT',
                 'GAGTCGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG',
                 'GACGGCAACTACGGTTACAACGCAGCAACCGAAGAATATT',
                 'TCTGTTGTTGCTAACACCGTTAAAGGCGGCGACGGCAACT',
                 'AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG',
                 'AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA']
# ['GAGGC', 'TCATC', 'TCGGC', 'GAGTC', 'GCAGC', 'GCGGC', 'GCGGC', 'GCATC']

# print(greedy_motif_search(dna_for_test1, 5, 8))
