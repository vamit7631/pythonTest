input =  ["eat","tea","tan","ate","nat","bat"]


def group_anagrams(input):
    anObj = {}
    for word in input:
        result = "".join(sorted(word))
        if result in anObj:
            anObj[result].append(word)
        else:
            anObj[result] = [word]
        
    return list(anObj.values())




print(group_anagrams(input)) # output : [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]