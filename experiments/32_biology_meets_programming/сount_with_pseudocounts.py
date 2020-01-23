

def count_with_pseudocounts(motifs):
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

    for key in count:
        count[key] = list(map(lambda x: x+1, count[key]))

    return count


def profile_with_pseudocounts(motifs):
    profile = count_with_pseudocounts(motifs)
    sums = [sum(row) for row in zip(*profile.values())]
    for key in profile:
        profile[key] = [x/y for x, y in zip(profile[key], sums)]
    return profile


motifs = ['AACGTA', 'CCCGTT', 'CACCTT', 'GGATTA', 'TTCCGG']
# print(profile_with_pseudocounts(motifs))
