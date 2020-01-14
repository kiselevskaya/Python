# symbol_array.py

Functions:

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


