"""
* @author agond
* @package main.slidingWindow.medium
* @Date 28/09/2023
* @Project PracticeDSA
* 1297. Maximum Number of Occurrences of a Substring
* Medium
* Topics
* Companies
* Hint
* Given a string s, return the maximum number of occurrences of any substring under the following rules:
* <p>
* The number of unique characters in the substring must be less than or equal to maxLetters.
* The substring size must be between minSize and maxSize inclusive.
* <p>
* Example 1:
* <p>
* Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
* Output: 2
* Explanation: Substring "aab" has 2 occurrences in the original string.
* It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
* Example 2:
* <p>
* Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
* Output: 2
* Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
* <p>
* Constraints:
* <p>
* 1 <= s.length <= 105
* 1 <= maxLetters <= 26
* 1 <= minSize <= maxSize <= min(26, s.length)
* s consists of only lowercase English letters.
"""


class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        n = len(s)
        substring_frequency = {}
        max_freq = 0
        i = 0

        while i <= n - minSize:
            sub_string = s[i: i + minSize]
            unique_chars = set()
            distinct_chars = 0

            for c in sub_string:
                if c not in unique_chars:
                    distinct_chars += 1
                    unique_chars.add(c)

            if distinct_chars <= maxLetters:
                substring_frequency[sub_string] = substring_frequency.get(sub_string, 0) + 1
                max_freq = max(max_freq, substring_frequency[sub_string])

            i += 1

        return max_freq


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
result = solution_instance.maxFreq(s, maxLetters, minSize, maxSize)

assert result == 2, "Test 1, should be equal to 2."

s = "aaaa"
maxLetters = 1
minSize = 3
maxSize = 3
result = solution_instance.maxFreq(s, maxLetters, minSize, maxSize)

assert result == 2, "Test 2, should be equal to 2."
