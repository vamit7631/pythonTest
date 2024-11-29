sampleArr = [10, 20, 15, 5, 12, 25, 13]

def largetNumber(sampleArr):
    largest = 0
    for i in range(len(sampleArr)):
            num = sampleArr[i]
            if num > largest:
                largest = num
    return largest

print(largetNumber(sampleArr))
##################### list comprehension ######################################

largest2 = max([x for x in sampleArr])
print(largest2)

