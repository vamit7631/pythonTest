sampleArr = [10, 20, 15, 5, 12, 25, 13,45]

def largestNumber(sampleArr):
    largest = 0
    for i in sampleArr:
            if i > largest:
               largest = i
    return largest

print(largestNumber(sampleArr))
##################### list comprehension ######################################

largest2 = max([x for x in sampleArr])
print(largest2)

