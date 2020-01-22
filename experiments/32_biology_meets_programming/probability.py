

from pattern_count import frequent_words


def probability(motif, profile):
    probable = 1
    for i in range(len(motif)):
        char = motif[i]
        probable *= profile[char][i]
    return probable


motif = 'ACGGGGATTACC'
profile = {'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
           'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
           'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
           'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
# print(probability(motif, profile))


# def profile_most_probable_kmer(text, k, profile):
#     motifs = frequent_words(text, k)
#     most_probable = ''
#     frequency = 0
#     for i in range(len(motifs)):
#         motif = motifs[i]
#         if probability(motif, profile) > frequency:
#             frequency = probability(motif, profile)
#             most_probable = motif
#     if most_probable == '':
#         most_probable = motifs[0]
#     return most_probable


def profile_most_probable_pattern(text, k, profile):
    p = -1
    most_probable = text[0:k]
    for i in range(len(text)-k+1):
        motif_to_compare = text[i:i+k]
        pr = probability(motif_to_compare, profile)
        if pr > p:
            p = pr
            most_probable = motif_to_compare
    return most_probable


k = 5
text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
ProfileTestCase0 = {'A': [0.2, 0.2, 0.3, 0.2, 0.3],
                    'C': [0.4, 0.3, 0.1, 0.5, 0.1],
                    'G': [0.3, 0.3, 0.5, 0.2, 0.4],
                    'T': [0.1, 0.2, 0.1, 0.1, 0.2]}
# output = 'CCGAG'

ProfileTestCase1 = {'A': [0.7, 0.2, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1],
                    'C': [0.2, 0.2, 0.5, 0.4, 0.2, 0.3, 0.1, 0.6],
                    'G': [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.4, 0.2],
                    'T': [0.0, 0.3, 0.2, 0.0, 0.2, 0.3, 0.3, 0.1]}
# output = 'AACAAACC'

ProfileTestCase2 = {'A': [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5],
                    'C': [0.3, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.4, 0.3, 0.2, 0.2, 0.1],
                    'G': [0.2, 0.1, 0.4, 0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1],
                    'T': [0.3, 0.4, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.4, 0.4, 0.2, 0.3]}
# output = 'GAACAAACCCAA'

ProfileTestCase3 = {'A': [1.0, 1.0, 1.0],
                    'C': [0.0, 0.0, 0.0],
                    'G': [0.0, 0.0, 0.0],
                    'T': [0.0, 0.0, 0.0]}
# output = 'CCT'


# print(profile_most_probable_kmer(text, k, ProfileTestCase0))
# print(profile_most_probable_kmer(text, 8, ProfileTestCase1))
# print(profile_most_probable_kmer(text, 12, ProfileTestCase2))
# print(profile_most_probable_kmer(text, 3, ProfileTestCase3))

# text = 'GAGCTA'
# ProfileTestCase4 = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
#                     'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
#                     'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
#                     'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
# #
# print(probability(text, ProfileTestCase4))


# Consider the following profile matrix:
# ProfileTestCase4 = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
#                     'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
#                     'G': [0., 0.3, 1.0, 0.1, 0.5, 0.0],
#                     'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}

# Which of the following strings is a consensus string for this profile matrix? (Select all that apply.)
#
# def get_consensus(profile):
#     k = 6
#     count = profile
#
#     consensus = ''
#     for j in range(k):
#         m = 0
#         frequent_symbol = ''
#         for symbol in "ACGT":
#             if count[symbol][j] > m:
#                 m = count[symbol][j]
#                 frequent_symbol = symbol
#         consensus += frequent_symbol
#     return consensus


# pr = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
#       'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
#       'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
#       'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
# print(get_consensus(pr))
