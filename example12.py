arr1 = ["apple", "ape", "april"] 
# arr2 = ["flower","flow","flight"]
# arr3 = ["apple", "banana", "apricot"]


def find_longest_prefix(words):
    if not words:
        return ""
    
    min_length = min(len(word) for word in words)
    print(min_length,"=========1")
    prefix = ""
    
    for i in range(min_length):
        chars = {word[i] for word in words}
        print(chars,"=========2===========", words[0][i])
        if len(chars) == 1:
            prefix = prefix + words[0][i]
            print(prefix,"=========3")
        else:
            break
    
    return prefix




print(find_longest_prefix(arr1)) # output =  "ap"
# print(find_longest_prefix(arr2)) #  output =  "fl"
# print(find_longest_prefix(arr3)) #  output =  ""
