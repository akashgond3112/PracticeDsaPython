"""
* @author agond
* @package main.slidingWindow.medium
* @Date 26/09/2023
* @Project PracticeDSA
* <p>
* 424. Longest Repeating Character Replacement
* Medium
* Topics
* Companies
* You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
* <p>
* Return the length of the longest substring containing the same letter you can get after performing the above operations.
* <p>
* Example 1:
* <p>
* Input: s = "ABAB", k = 2
* Output: 4
* Explanation: Replace the two 'A's with two 'B's or vice versa.
* Example 2:
* <p>
* Input: s = "AABABBA", k = 1
* Output: 4
* Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
* The substring "BBBB" has the longest repeating letters, which is 4.
* There may exists other ways to achive this answer too.
* <p>
* Constraints:
* <p>
* 1 <= s.length <= 105
* s consists of only uppercase English letters.
* 0 <= k <= s.length
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start_index = 0
        end_index = 0
        max_value = 0
        max_repeat_char = 0

        char_dic = {}

        while end_index < len(s):
            ch = s[end_index]
            char_dic[ch] = char_dic.get(ch, 0) + 1

            max_repeat_char = max(max_repeat_char, char_dic[ch])

            while end_index - start_index + 1 - max_repeat_char > k:
                ch = s[start_index]
                char_dic[ch] = char_dic.get(ch, 0) - 1
                start_index += 1

            max_value = max(max_value, end_index - start_index + 1)
            end_index += 1
        return max_value


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
str = "ABAB"
k = 2
result = solution_instance.characterReplacement(str, k)

assert result == 4, "Test 1, should be equal to 4."

str = "AABABBA"
k = 1
result = solution_instance.characterReplacement(str, k)
assert result == 4, "Test 2, should be equal to 4."
