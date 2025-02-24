arr1 = ["apple", "ape", "april"] 
arr2 = ["apple", "banana", "apricot"]


def find_longest_prefix(words):
    if not words:
        return ""
    
    min_length = min(len(word) for word in words)
    prefix = ""
    
    for i in range(min_length):
        chars = {word[i] for word in words}
        if len(chars) == 1:
            prefix += words[0][i]
        else:
            break
    
    return prefix




print(find_longest_prefix(arr1)) # output =  "ap"
print(find_longest_prefix(arr2)) #  output =  ""