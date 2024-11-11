sampleArr = [10, 20, 10, 15, 15, 12, 25, 13, 10, 25]


def repeatedNumber(sampleArr):
    count = {}
    for i in range(len(sampleArr)):
        num = sampleArr[i]
        if num in count:
            count[num] = count[num] + 1
        else:
            count[num] = 1

    return count 

print(repeatedNumber(sampleArr))