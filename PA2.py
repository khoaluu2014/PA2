#Khoa Luu
#09/30/22

from math import floor, inf


def maxSubArrayDivideAndConquer(nums: list[int]) -> int:
    p = 0
    r = len(nums)
    
    # 0 element
    if p == r:
        return 0
    # base case 1 element
    if r == 1:
        return nums[0]
    # recursive case
    q = floor(int((p + r) / 2))
    # max sum on the left
    leftSum = maxSubArrayDivideAndConquer(nums[p:q])
    # max sum on the right
    rightSum = maxSubArrayDivideAndConquer(nums[q + 1: r])
    # max sum in the middle
    midSum = maxSpan(nums, p, q, r)
    # max subarray
    return max(leftSum, rightSum, midSum)


def maxSpan(nums: list[int], p, q, r) -> int:
    # Find max sum to the left
    leftSum = -inf
    s = 0
    for i in range(q, p - 1, -1):
        s = s + nums[i]
        if s >= leftSum:
            leftSum = s
    # Find max sum to the right
    rightSum = -inf
    s = 0
    for i in range(q + 1, r, 1):
        s = s + nums[i]
        if s >= rightSum:
            rightSum = s
    maxSum = leftSum + rightSum
    return maxSum


# I read this in Introduction to Competitive Programming before.
# This is a smart approach given there's at least a negative int.
def maxSubArrayKadane(nums: list[int]) -> int:
    maxSoFar = -inf
    maxEndingHere = 0
    for i in range(0, len(nums)):
        maxEndingHere = maxEndingHere + nums[i]
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere
        if maxEndingHere < 0:
            maxEndingHere = 0
    return maxSoFar
