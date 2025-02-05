sampleArr = [10, 20, 10, 15, 15, 12, 25, 13, 10, 25]


def repeatedNumber(sampleArr):
    count = {}
    for i in sampleArr:
        if i in count:
            count[i] = count[i] + 1
        else:
            count[i] = 1

    return count 

print(repeatedNumber(sampleArr))