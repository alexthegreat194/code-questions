'''
Original question:
implement bubble sort
'''
def bubble_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

# test bubble_sort
print(bubble_sort([1,2,3,4,5]))
print(bubble_sort([5,4,3,2,1]))
print(bubble_sort([1, 5, 9, 8, 10, 6, 3, 7, 4, 2]))