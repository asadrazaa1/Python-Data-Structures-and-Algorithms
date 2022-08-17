def merge(s1, s2, s):
    """Merge two sorted lists s1, s2 into properly sized list z"""
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]      # copy ith element of s1 as next item of s
            i += 1
        else:
            s[i+j] = s2[j]      # copy jth element of s2 as next item of s
            j += 1


def merge_sort(S):
    """Sort elements of python list S using the merge-sort algorithm"""
    n = len(S)
    if n < 2:
        return      # list is already sorted
    # divide
    mid = n // 2
    s1 = S[0:mid]       # first half
    s2 = S[mid:n]       # second half
    # conquer
    merge_sort(s1)
    merge_sort(s2)
    merge(s1, s2, S)        # merge sorted halves back into S
    
