# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 
input1 = "anagram" 
input2 = "nagaram"
# input1 = "rat"
# input2 = "car"


##################### sort method ######################################

def testfunction(input1, input2):
    input1 = "".join(sorted(input1))
    input2 = "".join(sorted(input2))
    if input1 == input2:
        return True
    else:
        return False


print(testfunction(input1, input2))


##################### count method ######################################

from collections import Counter

def is_anagram(input1, input2):
    return Counter(input1) == Counter(input2)

# Example usage
print(is_anagram(input1, input2))  