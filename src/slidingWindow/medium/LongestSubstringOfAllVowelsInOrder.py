"""
 * @author agond
 * @package main.slidingWindow.medium
 * @Date 01/11/2023
 * @Project PracticeDSA
 * <p>
 * 1839. Longest Substring Of All Vowels in Order
 * Medium
 * Topics
 * Companies
 * Hint
 * A string is considered beautiful if it satisfies the following conditions:
 * <p>
 * Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
 * The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
 * For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.
 * <p>
 * Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.
 * <p>
 * A substring is a contiguous sequence of characters in a string.
 * <p>
 * Example 1:
 * <p>
 * Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
 * Output: 13
 * Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
 * Example 2:
 * <p>
 * Input: word = "aeeeiiiioooauuuaeiou"
 * Output: 5
 * Explanation: The longest beautiful substring in word is "aeiou" of length 5.
 * Example 3:
 * <p>
 * Input: word = "a"
 * Output: 0
 * Explanation: There is no beautiful substring, so return 0.
 * <p>
 * Constraints:
 * <p>
 * 1 <= word.length <= 5 * 105
 * word consists of characters 'a', 'e', 'i', 'o', and 'u'.
"""


class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """

        start_index = 0
        end_index = 1
        max_length = float('-inf')

        char_count = {}
        ch = word[0]
        char_count[ch] = 1

        while end_index < len(word):
            if word[end_index - 1] > word[end_index]:
                char_count.clear()
                start_index = end_index

            ch = word[end_index]
            char_count[ch] = char_count.get(ch, 0) + 1

            if len(char_count) == 5:
                max_length = max(max_length, end_index - start_index + 1)

            end_index += 1

        return max(max_length, 0)


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
result = solution_instance.longestBeautifulSubstring(word)

assert result == 13, "Test 1, should be equal to 13."

word = "aeeeiiiioooauuuaeiou"
result = solution_instance.longestBeautifulSubstring(word)
assert result == 5, "Test 2, should be equal to 5."

word = "a"
result = solution_instance.longestBeautifulSubstring(word)
assert result == 0, "Test 2, should be equal to 0."
