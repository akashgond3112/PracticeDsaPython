"""
 * @author agond
 * @package main.slidingWindow.medium
 * @Date 25/10/2023
 * @Project PracticeDSA
 * 1208. Get Equal Substrings Within Budget
 * Medium
 * Topics
 * Companies
 * Hint
 * You are given two strings s and t of the same length and an integer maxCost.
 * <p>
 * You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
 * <p>
 * Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.
 * <p>
 * Example 1:
 * <p>
 * Input: s = "abcd", t = "bcdf", maxCost = 3
 * Output: 3
 * Explanation: "abc" of s can change to "bcd".
 * That costs 3, so the maximum length is 3.
 * Example 2:
 * <p>
 * Input: s = "abcd", t = "cdef", maxCost = 3
 * Output: 1
 * Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
 * Example 3:
 * <p>
 * Input: s = "abcd", t = "acde", maxCost = 0
 * Output: 1
 * Explanation: You cannot make any change, so the maximum length is 1.
 * <p>
 * Constraints:
 * <p>
 * 1 <= s.length <= 105
 * t.length == s.length
 * 0 <= maxCost <= 106
 * s and t consist of only lowercase English letters.
"""


class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        actual_sum = 0
        start_index = 0
        end_index = 0
        max_value = 0

        while end_index < len(s):
            actual_sum += abs(ord(s[end_index]) - ord(t[end_index]))

            if actual_sum <= maxCost:
                max_value = max(max_value, end_index - start_index + 1)

            while actual_sum > maxCost:
                actual_sum -= abs(ord(s[start_index]) - ord(t[start_index]))
                start_index += 1
            end_index += 1

        return max_value


# Create an instance of the Solution class
solution_instance = Solution()

s = "abcd"
t = "bcdf"
maxCost = 3
result = solution_instance.equalSubstring(s, t, maxCost)
assert result == 3, "Test 1, should be equal to 3."

s = "abcd"
t = "cdef"
maxCost = 3
result = solution_instance.equalSubstring(s, t, maxCost)
assert result == 1, "Test 2, should be equal to 1."

s = "abcd"
t = "acde"
maxCost = 0
result = solution_instance.equalSubstring(s, t, maxCost)
assert result == 1, "Test 2, should be equal to 1."
