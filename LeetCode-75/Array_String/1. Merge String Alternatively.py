# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

# Solution 1
def mergeAlternatelySolution1(word1: str, word2: str) -> str:
    merged = []
    len1, len2 = len(word1), len(word2)
    min_len = min(len1, len2)

    for i in range(min_len):
        merged.append(word1[i])
        merged.append(word2[i])

    if len1 > len2:
        merged.append(word1[min_len:])
    else:
        merged.append(word2[min_len:])

    return ''.join(merged)

# Solution 2
def mergeAlternatelySolution2(word1: str, word2: str) -> str:
    merged = []
    i, j = 0, 0
    len1, len2 = len(word1), len(word2)

    while i < len1 or j < len2:
        if i < len1:
            merged.append(word1[i])
            i += 1
        if j < len2:
            merged.append(word2[j])
            j += 1

    return ''.join(merged)

# Solution 3
def mergeAlternatelySolution3(word1: str, word2: str) -> str:
    result = []
    n = max(len(word1), len(word2))
    for i in range(n):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]

    return "".join(result)

# Solution 4
def mergeAlternatelySolution4(word1: str, word2: str) -> str:
    from itertools import zip_longest
    merged = []
    
    for a, b in zip_longest(word1, word2, fillvalue=''):
        merged.append(a)
        merged.append(b)
    
    return ''.join(merged)

# Example usage:
word1 = "abcxyz"  
word2 = "pqr"
print(mergeAlternatelySolution1(word1, word2))  # Output: "apbq 
print(mergeAlternatelySolution2(word1, word2))  # Output: "apbq 
print(mergeAlternatelySolution3(word1, word2))  # Output: "apbq 
print(mergeAlternatelySolution4(word1, word2))  # Output: "apbq 
