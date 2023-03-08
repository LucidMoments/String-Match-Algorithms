def BruteForce(text, pattern):

    for i in range(len(text)-len(pattern)+1):
        index = i
        for j in range(len(pattern)):
            if text[index] == pattern[j]:
                index += 1
            else:
                break
        if index-i == len(pattern):
            return i
    return -1


