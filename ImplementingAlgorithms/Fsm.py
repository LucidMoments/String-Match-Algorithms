def engine(s, a, n, p):

    if n > s:
        m = s + 1
    else:
        m = n

    k = m

    while k > 0:
        if p[k - 1] == a:
            j = k - 2
            w = s - 1

            while j >= 0 and p[j] == p[w]:
                j -= 1
                w -= 1

            if j < 0:
                return k

        k -= 1

    return 0



def fsm(text, pattern):
    m = len(text)
    n = len(pattern)
    state = 0

    S: list[str] = sorted(set(pattern))

    for i in range(m):
        state = engine(state, text[i], n, pattern)
        if state == n:
            return i - n + 1

    return -1
