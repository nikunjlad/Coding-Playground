# fibonacci series using traditional recursion and using dynamic programming strategy


# Method 1: Using Recursion technique
import time

# start time for calculating program execution
start = time.time()

# define a function named fib which takes in the index of the fibonacci series and returns corresponding value


def fib(n):

    if n == 1 or n == 2:  # if number is 1 or 2 i.e the first and second element in the fibonacci series is going to be 1
        result = 1
    else:
        # recursively call the fibonacci function to calculate the fibonacci value
        result = fib(n - 1) + fib(n - 2)

    return result


print(fib(40))
stop = time.time()
print("Time elapsed: {} second(s)".format(str(round(stop - start, 2))))
print("\n")

# Method 2: Using Dynamic Programming
start2 = time.time()


def dyna_fib(n, memo):

    # check if the memoization array has tha value already stored in it, if yes then return the value
    if memo[n] != None:
        return memo[n]

    # if the element to be retrieved from the series is either 1,2 then result is 1, else we recursively compute the values
    if n <= 2:
        result = 1
    else:
        result = dyna_fib(n - 1, memo) + dyna_fib(n - 2, memo)

    # fill up the memoization array to avoid redundant recursive computations
    memo[n] = result
    return result

# function to initialize the memoization array and call the recursive function


def dyna_memo(n):
    memo = [None] * (n + 1)
    return dyna_fib(n, memo)


print(dyna_memo(40))
stop2 = time.time()
print("Time elapsed: {} second(s)".format(str(round(stop2 - start2, 2))))
print("\n")

# Method 3:  Using bottom up approach of using just arrays

# at one point, say n = 100000, the python recursive error occurs due to large computational depths


def dynamic(n):

    # check if 1st or 2nd element in the series is requested, if yes then return 1
    if n <= 2:
        return 1

    # dynamically keep building the memoization array
    memoize = [None] * (n + 1)

    # populate the 1st and 2nd series position with value 1 of the fibonacci series
    memoize[1] = 1
    memoize[2] = 2

    # for values beyond first 2 elements, i.e from 3 to n, compute the elements in the fibonacci series and populate the memoization
    # array on the fly, i.e value of the current state is sum of the values of previous 2 elements in the series
    for i in range(3, n + 1):
        memoize[i] = memoize[i - 1] + memoize[i - 2]

    return memoize[n]


print(dynamic(40))
