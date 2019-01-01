import sys

def max(*nums):
    max_n = -sys.maxsize - 1
    # print(max_n)
    print(nums)
    for n in nums:
        if max_n < n:
            max_n = n

    print("Max: ", max_n)


max(3, 5)
max(4, 5, 6, 7)
max(1, 2, 3, 5, 6)