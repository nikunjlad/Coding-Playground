"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []  # initialize a list

        # for every digit in the number
        for digit in num:

            # if value of k is not 0 and stack is full and last entered element in stack is bigger than current digit
            # since we want to find smallest number having dropped k elements, we need to check if the value pushed
            # in the stack is greater than current value. If yes, then we pop that element out and discard it and
            # decrement the k counter by 1. Every time we pop an element from the list we are essentially removing them
            # from the array and finding our way to the smallest number
            while k and stack and stack[-1] > digit:
                k -= 1  # decrement k
                stack.pop()  # pop out the last element from the stack

            # if previous digit pushed to stack is not greater than current digit, then append it to the stack
            stack.append(digit)

        # if value of k does not reduce to 0 by the time we loop over the digits, remove the elements from back of the
        # stack
        if k > 0:
            stack = stack[:-k]  # truncate values from end of stack if k value > 0

        return "".join(stack).lstrip("0") or "0"


s = Solution()
print("Smallest possible number removing 3 digits from 1432219 is {}".format(s.removeKdigits("1432219", 3)))
print("Smallest possible number removing 1 digits from 10200 is {}".format(s.removeKdigits("10200", 1)))
print("Smallest possible number removing 2 digits from 10 is {}".format(s.removeKdigits("10", 2)))
