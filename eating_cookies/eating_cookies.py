'''
Input: an integer
Returns: an integer
'''
# cookie monster can eat either 1, 2, or 3 cookies at once
# find all possible ways to reach `n` cookies
# count each different way to reach `n` cookies
# return number of possible ways to reach `n`

def eating_cookies(n):
    total = 0
    if n <= 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        total += eating_cookies(n-1)
        total += eating_cookies(n-2)
        total += eating_cookies(n-3)
    return total

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
