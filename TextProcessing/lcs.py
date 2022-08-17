def LCS(X, Y):
    """Lowest common subsequence

    Return table such that L[j][k] is the length of LCS for X[0:j] and Y[0:k]"""
    n, m = len(X), len(Y)
    L = [[0]*(m+1) for k in range(n+1)]     # (n+1) x (m+1) table
    for j in range(n):
        for k in range(m):
            if X[j] == Y[k]:            # align this match
                L[j+1][k+1] = L[j][k] + 1
            else:           # choose to ignore one character
                L[j+1][k+1] = max(L[j][k+1], L[j+1][k])
    return L
