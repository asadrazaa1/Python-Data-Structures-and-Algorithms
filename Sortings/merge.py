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

