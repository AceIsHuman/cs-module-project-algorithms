'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# Understand

# We will look at `k` values from left to right and store the largest value
# `k` determines the size of our viewing window
# the end of the window must not pass the last index of list
# after each pass move window start and end positions to right by one index
# return list of all stored largest values

def sliding_window_max(nums, k):
    # create window start and end indices
    start, end = 0, k - 1
    # create list to store max values
    max_vals = []
    # while end is less than length of nums
    while end < len(nums):
    ## compare values in window and add largest to max values
        max_num = compare_window(nums, start, end)
        max_vals.append(max_num)
    ## once compare is complete increase window indices
        start += 1
        end += 1
    # return max values
    return max_vals

def compare_window(nums, start, end):
    pointer = start + 1
    max_num = nums[start]
    while pointer <= end:
        if max_num < nums[pointer]:
            max_num = nums[pointer]
        pointer += 1
    return max_num

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
