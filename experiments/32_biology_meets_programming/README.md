

# symbol_array.py


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




# humming_distance.py

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




# score_motifs.py

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
    Compare the i-th nucleotide of each k-mer of motifs with i-th nucleotide of consensus string

    Input:  A list of k-mers motifs
    Output: number of all mismatches

