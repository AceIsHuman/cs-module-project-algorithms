'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # eliminate all numbers that occur twice
    for i in range(len(arr)):
        if arr[i] is None:
            # skip is arr[i] is has already been checked
            pass
        try:
            # save current value
            val = arr[i]
            # assign current index value to None
            arr[i] = None
            # if error on accessing a second value, this is the single_number
            second = arr.index(val)
            # if second valu exists also assign that position to None
            arr[second] = None
        except ValueError:
            # return remaining number
            return val


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")