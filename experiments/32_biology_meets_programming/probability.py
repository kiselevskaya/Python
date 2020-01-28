

def probability(motif, profile):
    probable = 1
    for i in range(len(motif)):
        char = motif[i]
        probable *= profile[char][i]
    return probable


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


def get_consensus_profile(profile, k):
    count = profile
    consensus = ''
    for j in range(k):
        m = 0
        frequent_symbol = ''
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequent_symbol = symbol
        consensus += frequent_symbol
    return consensus


# if __name__ == '__main__':
#     # Test_0 probability(motif, profile)
#     motif0 = 'ACGGGGATTACC'
#     profile0 = {'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
#                 'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
#                 'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
#                 'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]}
#     print(probability(motif0, profile0))
#
#     # Test_1 probability(motif, profile) Output 'CCT'
#     text1 = 'GAGCTA'
#     profile1 = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
#                 'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
#                 'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
#                 'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
#     print(probability(text1, profile1))
#
#     text = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
#     # Test_2 profile_most_probable_pattern(text, k, profile) Output 'CCGAG'
#     profile2 = {'A': [0.2, 0.2, 0.3, 0.2, 0.3],
#                 'C': [0.4, 0.3, 0.1, 0.5, 0.1],
#                 'G': [0.3, 0.3, 0.5, 0.2, 0.4],
#                 'T': [0.1, 0.2, 0.1, 0.1, 0.2]}
#     print(profile_most_probable_pattern(text, 5, profile2))
#
#     # Test_3 profile_most_probable_pattern(text, k, profile) Output 'AACAAACC'
#     profile3 = {'A': [0.7, 0.2, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1],
#                 'C': [0.2, 0.2, 0.5, 0.4, 0.2, 0.3, 0.1, 0.6],
#                 'G': [0.1, 0.3, 0.2, 0.1, 0.2, 0.1, 0.4, 0.2],
#                 'T': [0.0, 0.3, 0.2, 0.0, 0.2, 0.3, 0.3, 0.1]}
#     print(profile_most_probable_pattern(text, 8, profile3))
#
#     # Test_4 profile_most_probable_pattern(text, k, profile) Output 'GAACAAACCCAA'
#     profile4 = {'A': [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5],
#                 'C': [0.3, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.4, 0.3, 0.2, 0.2, 0.1],
#                 'G': [0.2, 0.1, 0.4, 0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1],
#                 'T': [0.3, 0.4, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.4, 0.4, 0.2, 0.3]}
#     print(profile_most_probable_pattern(text, 12, profile4))
#
#     # Test_5 profile_most_probable_pattern(text, k, profile) Output 'CCT'
#     profile5 = {'A': [1.0, 1.0, 1.0],
#                 'C': [0.0, 0.0, 0.0],
#                 'G': [0.0, 0.0, 0.0],
#                 'T': [0.0, 0.0, 0.0]}
#     print(profile_most_probable_pattern(text, 3, profile5))
#
#     # Test_6 get_consensus_profile(profile, k)
#     # Consider the following profile matrix:
#     profile6 = {'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
#                 'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
#                 'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
#                 'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}
#     # Which of the following strings is a consensus string for this profile matrix? (Select all that apply.)
#     print(get_consensus_profile(profile6, 6))
