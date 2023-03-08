def sunday_find(text, pattern):
    m = len(text)
    n = len(pattern)

    A = list(range(128))
    for a in range(128):
        A[a] = n + 1

    for j in range(n):
        A[ord(pattern[j])] = n - j

    for i in range(m - n):
        j = 0
        while j < n and (text[i + j] == pattern[j]):
            j += 1

        if j == n:
            return j

    return -1
