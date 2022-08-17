def LCS_solution(X, Y, L):
    """Longest common subsequence

    Return the longest common substring of X and Y, given LCS table L"""
    j, k = len(X), len(Y)
    solution = []
    while L[j][k] > 0:      # common characters remain
        if X[j-1] == Y[k-1]:
            solution.append(X[j-1])
            j -= 1
            k -= 1
        elif L[j-1][k] >= L[j][k-1]:
            j -= 1
        else:
            k -= 1
    return ''.join(reversed(solution))  # return let-to-right version
