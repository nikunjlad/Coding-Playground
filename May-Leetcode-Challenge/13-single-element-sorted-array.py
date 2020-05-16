"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sum(set(nums)) * 2 - sum(nums)


s = Solution()
print("Single element in sorted array [1,1,2,3,3,4,4,8,8] is {}".format(s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])))
print("Single element in sorted array [3,3,7,7,10,11,11] is {}".format(s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])))
