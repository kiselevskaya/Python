

# Input:  a set of k-mers (string) motifs
# Output: dictionary of lists with counted motif nucleotides

# def get_count(motifs):      # can be modify to profile_matrix(motifs)
#     count = {}  # initializing the count dictionary
#
#     # initializing and use the profile dictionary instead of counts to modify the function to get profile_matrix of motifs
#     # profile = {}
#
#     k = len(motifs[0])
#
#     #   counts = {'A':[]} --> counts = {'A':[0, 0, 0, 0, 0, 0], 'C':[]}
#     for symbol in "ACGT":
#         count[symbol] = []
#         # profile[symbol] = []
#
#         # counts = {'A':[0, 0, 0, 0, 0, 0]} -> counts = {'A':[0, 0, 0, 0, 0, 0], 'C':[0, 0, 0, 0, 0, 0]} ...
#         for j in range(k):
#             count[symbol].append(0)
#             # profile[symbol].append(0)
#
#     t = len(motifs)
#     for i in range(t):
#         for j in range(k):
#             symbol = motifs[i][j]  # 'A'
#             count[symbol][j] += 1
#             # profile[symbol][j] += float(1/t)
#         #   counts = {'A':[1, 1, 0, 0, 0, 1], 'C':[0, 0, 1, 0, 0, 0], 'G':[0, 0, 0, 1, 0, 0], 'T':[0, 0, 0, 0, 1, 0]}
#
#     return count


def get_count(motifs):
    count = {}
    k = len(motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(motifs)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            count[symbol][j] += 1

    return count


def profile_matrix(motifs):
    t = len(motifs)
    profile = get_count(motifs)
    for key in profile:
        profile[key] = [float(round(counts/t, 1)) for counts in profile[key]]
    return profile


# consensus string
#  most popular nucleotides in each column (the same position of each k_mer) of the motif matrix (ties are broken arbitrarily)
def get_consensus(motifs):
    # if len(motifs[0]) == 1:
    #     for i in range(len(motifs)):
    #         motifs[i] = list(motifs[i][0])

    k = len(motifs[0])
    count = get_count(motifs)

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


def get_score(motifs):
    consensus = list(get_consensus(motifs))
    mismatches = 0
    for motif in motifs:
        mismatches += sum(1 for i, j in zip(motif, consensus) if i != j)
    return mismatches


motifs = [['AACGTA'], ['CCCGTT'], ['CACCTT'], ['GGATTA'], ['TTCCGG']]

if len(motifs[0]) == 1:
    for i in range(len(motifs)):
        motifs[i] = list(motifs[i][0])


# print(get_score(motifs))
