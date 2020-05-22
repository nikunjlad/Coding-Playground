"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1

"""

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        count = 0

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if matrix[row - 1][col - 1] == 1:
                    dp[row][col] = 1 + min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1])
                    count += dp[row][col]

        return count


s = Solution()
mat1 = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
mat2 = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
print("Number of square submatrices in matrix {} are {}".format(str(mat1), str(s.countSquares(mat1))))
print("Number of square submatrices in matrix {} are {}".format(str(mat2), str(s.countSquares(mat2))))
