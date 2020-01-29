

import random
from probability import *


def normalize(probabilities):
    total = sum(probabilities.values())
    normalized = {k: probabilities[k] / total for k in probabilities}
    return normalized


def weighted_die(probabilities):
    r = random.uniform(0, 1)
    for key in probabilities:
        r -= probabilities[key]
        if r <= 0:
            return key


def profile_generated_string(text, profile, k):
    n = len(text)
    probabilities = {}
    for i in range(0, n-k+1):
        probabilities[text[i:i+k]] = probability(text[i:i+k], profile)
    probabilities = normalize(probabilities)
    return weighted_die(probabilities)


# if __name__ == '__main__':
#     # Test_1 normalize(probabilities) Output {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
#     probabilities1 = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
#     print(normalize(probabilities1))
#
#     # Test_2 weighted_die(probabilities)
#     probabilities2 = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
#     print(weighted_die(probabilities2))
#
#     # Test_3 profile_generated_string(text, profile, k)
#     text3 = 'AAACCCAAACCC'
#     profile3 = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
#     k3 = 2
#     print(profile_generated_string(text3, profile3, k3))
