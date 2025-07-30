import re 

def all_unique_substrings(s):
    substringArr = []
    for i in range(len(s)):
        unique_chars = ""
        for j in range(i, len(s)):
            if s[j] in unique_chars:
                break
            unique_chars = unique_chars + s[j]
            # print(i,"=======",s[j],"==============================")
        # print(unique_chars,"====================1")
        substringArr.append(unique_chars)
    print(substringArr)
    return substringArr


def longest_unique_substring(s):
    substrings = all_unique_substrings(s)
    print(substrings,"=====================1")
    return max(substrings, key = len)

# Test
input_str = "asddrewss"
print(longest_unique_substring(input_str))  # Output: drews
