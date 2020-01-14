

def hamming_distance(p, q):
    mismatches = []
    if len(p) != len(q):
        return 'Input strings must be equal'
    for i in range(len(p)):
        if p[i] != q[i]:
            mismatches.append(i)
    return len(mismatches)


def approximate_pattern_matching(text, pattern, d):
    positions = []
    last_check_index = len(text)-len(pattern)+1
    for i in range(last_check_index):
        compare_pattern = text[i:i+len(pattern)]
        mismatches = hamming_distance(compare_pattern, pattern)
        if d >= mismatches:
            positions.append(i)
    return positions


def approximate_pattern_count(text, pattern, d):
    count = 0
    last_check_index = len(text)-len(pattern)+1
    for i in range(last_check_index):
        compare_pattern = text[i:i+len(pattern)]
        mismatches = hamming_distance(compare_pattern, pattern)
        if d >= mismatches:
            count += 1
    return count
