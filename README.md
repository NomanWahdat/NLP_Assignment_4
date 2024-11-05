# NLP_Assignment_4

Edit Distance and Sequence Alignment
Overview
This report summarizes the implementation of algorithms for calculating Minimum Edit Distance and Needleman-Wunsch sequence alignment.

1. Minimum Edit Distance (Levenshtein Distance)
Purpose: Calculates the minimum number of operations (insertions, deletions, substitutions) to transform one string into another.
Implementation:
Initializes a distance matrix and a traceback matrix.
Fills the matrix based on operation costs.
Returns both the distance matrix and the operations required for transformation.
Key Function:
edit_distance(s1, s2, insert_cost=1, delete_cost=1, substitute_cost=1)
2. Traceback of Edit Operations
Purpose: Identifies the specific operations needed to convert one string to another.
Implementation:
traceback_operations(traceback, s1, s2) returns a list of operations.
3. Edit Distance Table Generation
Function:
print_edit_distance_table(dp, s1, s2) prints the distance matrix in a formatted manner.
4. Weighted Edit Distance
Purpose: Allows custom costs for insertions, deletions, and substitutions.
Key Function:
weighted_edit_distance(s1, s2, insert_cost, delete_cost, substitute_cost) recalculates distances using specified costs.
5. Phonetic Matching
Purpose: Computes edit distance based on phonetic similarity using the Soundex algorithm.
Key Functions:
soundex(name) generates a Soundex code for a name.
phonetic_edit_distance(s1, s2) calculates edit distance based on Soundex codes.
6. Needleman-Wunsch Alignment
Purpose: Finds the optimal alignment score between two sequences with gap penalties.
Implementation:
Builds a scoring matrix with match/mismatch and gap penalties.
Key Functions:
needleman_wunsch(s1, s2, gap_penalty, match_score, mismatch_penalty) computes the alignment.
traceback_nw(traceback, s1, s2) returns aligned sequences with gaps indicated.
Conclusion
The algorithms implemented for Minimum Edit Distance and Needleman-Wunsch alignment provide essential tools for string comparison and manipulation, applicable in various fields such as computational linguistics and bioinformatics.
