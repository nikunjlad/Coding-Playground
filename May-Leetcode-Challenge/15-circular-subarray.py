"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when
0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i],
C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:

        # this function is Kadane's algorithm implementation
        def maxSubArray(nums):
            current_max = global_max = nums[0]  # intially global and current max value is 0th element of list

            for i in range(len(nums) - 1):  # loop over all elements in the array

                # check maximum from (current value) and (sum of previous and current value)
                current_max = max(nums[i + 1], current_max + nums[i + 1])

                # if current max > global max, update global maximum
                if current_max > global_max:
                    global_max = current_max

            return global_max

        cs = sum(A)  # find sum of all elements in the array
        k = maxSubArray(A)  # find max-subarray of given list (Kadane value)
        neg_k = maxSubArray([x * -1 for x in A])  # find max-subarray of  list (Kadane value)
        cs += neg_k
        if cs > k and cs != 0:
            return cs
        else:
            return k


s = Solution()
print(
    "Maximum subarray sum of circular array [1,-2,3,-2] is : {}".format(str(s.maxSubarraySumCircular([1, -2, 3, -2]))))
print("Maximum subarray sum of circular array [5,-3,5] is : {}".format(str(s.maxSubarraySumCircular([5, -3, 5]))))
print(
    "Maximum subarray sum of circular array [3,-1,2,-1] is : {}".format(str(s.maxSubarraySumCircular([3, -1, 2, -1]))))
print(
    "Maximum subarray sum of circular array [3,-2,2,-3] is : {}".format(str(s.maxSubarraySumCircular([3, -2, 2, -3]))))
print("Maximum subarray sum of circular array [-2,-3,-1] is : {}".format(str(s.maxSubarraySumCircular([-2, -3, -1]))))
