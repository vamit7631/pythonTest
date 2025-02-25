nums = [3,2,2,3] 
val = 3

nums1 = [0,1,2,2,3,0,4,2]
val1 = 2


def removeElement(nums, val):
    result = [num for num in nums if num != val ]
    print(nums,"=================", result)
    result += ["_"] * (len(nums) - len(result))  # Fill remaining space with '_'
    return result


print(removeElement(nums, val)) # [2, 2, '_', '_']
print(removeElement(nums1, val1)) # [0, 1, 3, 0, 4, '_', '_', '_']