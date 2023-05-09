# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

def findMin(self, nums) -> int:
    if len(nums) == 1:
        return nums[0]
    
    last = nums[0]
    for i in range(len(nums) - 1):
        if nums[i + 1] < last:
            return nums[i + 1]
        last = nums[i + 1]
    return nums[0]

nums = [3,4,5,1,2]
print(findMin(nums))