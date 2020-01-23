

#   symbol_array.py

symbol_array:
    Input: Genome text as <genome> and <symbol> for eg. 'G'(guanine), 'C' (cytosine), 'A', 'T'
    Output:
        - counts the symbol at each position in genome text
        - returns dictionary;


faster_symbol_array:
    Input: <genome> and <symbol>
    Output:
        - do the same as symbol_array but consuming less time


skew_array:
    Input: <genome>
    Output:
        - returns list of difference in 'G'and 'C' at each position
        - list length equals genome length


minimum_skew:
    Input: <genome>
    Output:
        - list of positions with a minimum amount of guanine 'G'
        - the lowest points on a graph




#   humming_distance.py

We say that position i in k-mers p and q is a mismatch if the symbols at position i of the two strings are not the same.
The total number of mismatches between strings p and q is called the Hamming distance between these strings.


hamming_distance:
    Hamming Distance Problem:  Compute the Hamming distance between two strings.

    Input: Two strings <p> and <q> of equal length.
     Output: The Hamming distance between these strings.


approximate_pattern_matching:
    Approximate Pattern Matching Problem:  Find all approximate occurrences of a pattern in a string.

    Input: Strings <pattern> and <text> along with an integer <d>.
    Output: All starting positions where <pattern> appears as a substring of <text> with at most <d> mismatches.


approximate_pattern_count:
    This function computes the number of occurrences of <pattern> in <text> with at most <d> mismatches.




#   score_motifs.py

get_count:
    Function takes a list of strings <motifs> as input and returns the count matrix of <motifs> (as a dictionary of lists)

    Input:  a set of k-mers (string) motifs
    Output: dictionary of lists with counted motif nucleotides


profile_matrix:
    Profile matrix is the number of occurrences of the i-th nucleotide (each nucleotide at each position of k-mer)
        divided by t, the number of nucleotides in the column (the number of k-mers in motifs);
        (divide each element of the count matrix by the number of rows in the count matrix)

    Input:  A list of k-mers motifs
    Output: the profile matrix of motifs, as a dictionary of lists


get_consensus:
    Consensus string is a string of most popular nucleotides in each column of the motif matrix

    Input:  A list of k-mers motifs
    Output: Consensus string


get_score:
    Compare the i-th nucleotide of each k-mer of motifs with i-th nucleotide of consensus string.

    Input:  A list of k-mers motifs
    Output: number of all mismatches




#   probability.py

probability:
    Generating a random string based on a profile matrix by selecting the i-th nucleotide in the string with the probability corresponding to that nucleotide in the i-th column of the profile matrix.
    The probability that a profile matrix will produce a given string is given by the product of individual nucleotide probabilities.


profile_most_probable_kmer:
    Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
        Input: A string <text>, an integer <k>, and a 4 x <k> matrix Profile.
        Output: A Profile-most probable k-mer in <text>.




#   greedy_motif_search

    Greedy algorithms select the “most attractive” alternative at each iteration.
         For example, a greedy algorithm in chess might attempt to capture an opponent’s most valuable piece at every move.
         Yet anyone who has played chess knows that a strategy looking only one move ahead will likely produce disastrous results.
    In general, most greedy algorithms typically fail to find an exact solution of the problem; instead,
    they are often fast heuristics that trade accuracy for speed in order to find an approximate solution.


greedy_motif_search:
    Used get_score(motifs), get_count(motifs), profile_matrix(motifs), and get_consensus(motifs) functions.
    Used profile_most_probable_pattern(text, k, profile) and probability(text, profile) functions here.

    Input:  A list of k-mers <dna>, and integers <k> and <t> (where <t> is the number of k-mers in <dna>)
    Output: greedy_motif_search(dna, k, t)
    http://www.mrgraeme.co.uk/greedy-motif-search/




#   Entropy

    Entropy is a measure of the uncertainty of a probability distribution.
    The entropy of the completely conserved third column of the profile matrix in the figure in the first step is 0,
    which is the minimum possible entropy.
    On the other hand, a column with equally-likely nucleotides (all probabilities equal to 1/4)
     has maximum possible entropy 4 · 1/4 · log2 (1/4) = 2. In general, the more conserved the column, the smaller its entropy.


entropy:
     Compute the entropy of the motif matrix.




#   count_with_pseudocounts.py


count_with_pseudocounts:
    Function takes a list of strings <motifs> as input and returns the count matrix of <motifs> with pseudocounts (added a small number) as a dictionary of lists.


profile_with_pseudocounts:
    Function takes a list of strings <motifs> as input and returns the profile matrix of <motifs> with pseudocounts as a dictionary of lists.




#   greedy_with_pseudocounts.py


greedy_motif_search_with_pseudocounts:
    Function takes a list of strings <dna> followed by integers <k> and <t> and returns the result of running greedy_motif_search, where each profile matrix is generated with pseudocounts.
