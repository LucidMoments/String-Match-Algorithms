def KMP(text, pattern):

    if not pattern:
        return -1


    if not text or len(pattern) > len(text):
        return -1

    chars = list(pattern)


    next = [0] * (len(pattern) + 1)

    for i in range(1, len(pattern)):
        j = next[i + 1]

        while j > 0 and chars[j] is not chars[i]:
            j = next[j]

        if j > 0 or chars[j] == chars[i]:
            next[i + 1] = j + 1

    j = 0
    for i in range(len(text)):
        if j < len(pattern) and text[i] == pattern[j]:
            j = j + 1
            if j == len(pattern):
                return i - j + 1


        elif j > 0:
            j = next[j]
            i = i - 1
