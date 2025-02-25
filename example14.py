nums = [1,1,2]
nums1 = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums):
    result = sorted(set(nums))
    k = len(result)
    nums[:k] = result
    nums[k:] = ['_'] * (len(nums) - k)
    return k



print(removeDuplicates(nums), nums) # 2 [1, 2, '_']
print(removeDuplicates(nums1), nums1) # 5 [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']