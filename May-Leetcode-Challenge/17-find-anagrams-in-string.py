"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input: s: "cbaebabacd" p: "abc"
Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:   s: "abab" p: "ab"
Output:  [0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""

from typing import List
from collections import Counter


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:

        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []

        pc = Counter(p)
        sc = Counter()

        result = []
        for i in range(s_len):
            sc[s[i]] += 1
            if i >= p_len:
                if sc[s[i - p_len]] == 1:
                    del sc[s[i - p_len]]
                else:
                    sc[s[i - p_len]] -= 1

            if sc == pc:
                result.append(i - p_len + 1)

        return result


s = Solution()
print("Anagrams of 'abc' in string is 'cbaebabacd' is {}".format(str(s.findAnagrams('cbaebabacd', 'abc'))))
print("Anagrams of 'ab' in string is 'abab' is {}".format(str(s.findAnagrams('abab', 'ab'))))
