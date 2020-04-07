"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

Needs revision!
"""

from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        vals = dict()
        for num in nums:
            if num in vals:
                vals[num] += 1
            else:
                vals[num] = 1

        return list(vals.keys())[list(vals.values()).index(1)]


s = Solution()
nums = [4,1,2,1,2]
n = s.singleNumber(nums)
print(n)