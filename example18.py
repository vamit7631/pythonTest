# Merge Strings Alternately
word1 = "abc"
word2 = "pqr"
# Output: "apbqcr"
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"

def mergeAlternately(word1, word2):
    arr = []
    len1 = len(word1)
    len2 = len(word2)
    for i in range(max(len1, len2)):
        if i < len1:
            arr.append(word1[i])
        if i < len2:
            arr.append(word2[i])
    return "".join(arr)


print(mergeAlternately(word1,word2))