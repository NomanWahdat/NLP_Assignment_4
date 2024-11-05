# Minimum Edit Distance with Traceback

def edit_distance(s1, s2, insert_cost=1, delete_cost=1, substitute_cost=1):
    # Your implementation here

    # Initialize the distance matrix
    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Initialize traceback matrix
    traceback = [[None for _ in range(m + 1)] for _ in range(n + 1)]

    # Fill the first row and column
    for i in range(1, n + 1):
        dp[i][0] = i
        traceback[i][0] = 'D'  # Deletion

    for j in range(1, m + 1):
        dp[0][j] = j
        traceback[0][j] = 'I'  # Insertion

    # Fill the rest of the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = dp[i][j - 1] + 1
            deletion = dp[i - 1][j] + 1
            substitution = dp[i - 1][j - 1] + (0 if s1[i - 1] == s2[j - 1] else 1)

            # Choose the minimum operation cost
            dp[i][j] = min(insertion, deletion, substitution)

            # Traceback step
            if dp[i][j] == insertion:
                traceback[i][j] = 'I'
            elif dp[i][j] == deletion:
                traceback[i][j] = 'D'
            else:
                traceback[i][j] = 'S' if s1[i - 1] != s2[j - 1] else 'M'  # Substitution or Match

    return dp, traceback

def traceback_operations(traceback, s1, s2):
    i, j = len(s1), len(s2)
    operations = []

    while i > 0 or j > 0:
        operation = traceback[i][j]
        if operation == 'D':  # Deletion
            operations.append(f"Delete '{s1[i - 1]}' from s1")
            i -= 1
        elif operation == 'I':  # Insertion
            operations.append(f"Insert '{s2[j - 1]}' into s1")
            j -= 1
        elif operation == 'S':  # Substitution
            operations.append(f"Substitute '{s1[i - 1]}' in s1 with '{s2[j - 1]}'")
            i -= 1
            j -= 1
        else:  # Match
            operations.append(f"Match '{s1[i - 1]}'")
            i -= 1
            j -= 1

    return operations[::-1]  # Reverse to show operations in correct order

# Example usage
s1 = "kitten"
s2 = "sitting"
dp, traceback_matrix = edit_distance(s1, s2)

# Print the edit distance matrix
print("Edit Distance Matrix:")
for row in dp:
    print(row)

# Print traceback operations
print("\nOperations:")
for op in traceback_operations(traceback_matrix, s1, s2):
    print(op)

def print_edit_distance_table(dp, s1, s2):
    n, m = len(s1), len(s2)
    print("    ", "  ".join([" "] + list(s2)))
    print("   ", "-" * (3 * (m + 1)))
    for i in range(n + 1):
        row_label = s1[i - 1] if i > 0 else " "
        print(f"{row_label} |", "  ".join(map(str, dp[i])))

def weighted_edit_distance(s1, s2, insert_cost=1, delete_cost=1, substitute_cost=1):
    dp, traceback = edit_distance(s1, s2, insert_cost, delete_cost, substitute_cost)
    dp = edit_distance(s1, s2)  # Call it with only s1 and s2

    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i * delete_cost
    for j in range(1, m + 1):
        dp[0][j] = j * insert_cost

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = dp[i][j - 1] + insert_cost
            deletion = dp[i - 1][j] + delete_cost
            substitution = dp[i - 1][j - 1] + (0 if s1[i - 1] == s2[j - 1] else substitute_cost)
            dp[i][j] = min(insertion, deletion, substitution)

    return dp

def soundex(name):
    name = name.upper()
    soundex_mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    first_letter = name[0]
    tail = name[1:]

    tail = ''.join([soundex_mapping.get(char, '') for char in tail])
    tail = first_letter + ''.join([c for i, c in enumerate(tail) if i == 0 or tail[i] != tail[i-1]])
    tail = tail.replace('0', '')

    return (tail + '000')[:4]

def phonetic_edit_distance(s1, s2):
    code1 = soundex(s1)
    code2 = soundex(s2)
    return edit_distance(code1, code2)[0][-1][-1]

def needleman_wunsch(s1, s2, gap_penalty=1, match_score=1, mismatch_penalty=1):
    n, m = len(s1), len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    traceback = [[None for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][0] - gap_penalty
        traceback[i][0] = 'U'
    for j in range(1, m + 1):
        dp[0][j] = dp[0][j - 1] - gap_penalty
        traceback[0][j] = 'L'

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = dp[i - 1][j - 1] + (match_score if s1[i - 1] == s2[j - 1] else -mismatch_penalty)
            delete = dp[i - 1][j] - gap_penalty
            insert = dp[i][j - 1] - gap_penalty
            dp[i][j] = max(match, delete, insert)

            if dp[i][j] == match:
                traceback[i][j] = 'D'
            elif dp[i][j] == delete:
                traceback[i][j] = 'U'
            else:
                traceback[i][j] = 'L'

    return dp, traceback

def traceback_nw(traceback, s1, s2):
    alignment1 = []
    alignment2 = []
    i, j = len(s1), len(s2)

    while i > 0 or j > 0:
        if traceback[i][j] == 'D':
            alignment1.append(s1[i - 1])
            alignment2.append(s2[j - 1])
            i -= 1
            j -= 1
        elif traceback[i][j] == 'U':
            alignment1.append(s1[i - 1])
            alignment2.append('-')
            i -= 1
        else:  # 'L'
            alignment1.append('-')
            alignment2.append(s2[j - 1])
            j -= 1

    return ''.join(reversed(alignment1)), ''.join(reversed(alignment2))
