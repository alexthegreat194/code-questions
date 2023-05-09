'''
Implement Binary Search
use binary search to find the index of val in lys

input: 
    lys: list of sorted numbers
    val: number we want to find
output:
    index: index of the number in the list
'''

def BinarySearch(lys: list, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

def test_search(input_list, number_to_find):
    index = BinarySearch(input_list, number_to_find)
    if index != -1:
        print("Found at index:", index)
    else:
        print("Not found")

# use test_search to test your code
test_search([1,2,3,4,5,6,7,8,9,10], 5)
test_search([1,2,3,4,5,6,7,8,9,10], 11)