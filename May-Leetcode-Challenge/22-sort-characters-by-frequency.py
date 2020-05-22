"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

"""
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        letter = Counter(s)
        return "".join(
            [item[0] * item[1] for item in sorted(list(letter.items()), key=lambda item: item[1], reverse=True)])


s = Solution()
print("Frequency sort of word tree in reverse order is {}".format(s.frequencySort("tree")))
print("Frequency sort of word cccaaa in reverse order is {}".format(s.frequencySort("cccaaa")))
print("Frequency sort of word Aabb in reverse order is {}".format(s.frequencySort("Aabb")))
