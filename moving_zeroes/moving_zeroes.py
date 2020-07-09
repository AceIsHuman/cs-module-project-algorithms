'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # get start index
    start = 0
    # get end index
    end = len(arr) - 1

    # if start index == 0 move to end and shift rest to left
    while start < end:
        if arr[start] == 0:
            pointer = start
            # replace pointer index with next value
            while pointer < end:
                arr[pointer] = arr[pointer + 1]
                pointer += 1
            # assign ending value to 0 and decrement index
            arr[end] = 0
            end -= 1
        else:
            # if number is not zero, move start to next index
            start += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")