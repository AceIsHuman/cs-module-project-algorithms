'''
Input: a List of integers
Returns: a List of integers
'''
# multiply all values except current index value
# assign product to the current index

def product_of_all_other_numbers(arr):
    # create products list matching length of input list
    products = [0] * len(arr)
    # store ending index
    end = len(arr) - 1
    # iterate over list
    for i in range(len(arr)):
        ## create starting product variable
        ## create pointer starting at 0 index
        product, pointer = 1, 0
        ## multiply entire list, while excluding current index
        while pointer <= end:
            if pointer != i:
                product *= arr[pointer]
            pointer += 1
        ## add product to products list at current index
        products[i] = product

    # return products list
    return products

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
