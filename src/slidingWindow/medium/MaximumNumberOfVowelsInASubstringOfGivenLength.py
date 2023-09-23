"""

* @author agond
* @package main.slidingWindow.medium
* @Date 23/09/2023
* @Project PracticeDSA

1456. Maximum Number of Vowels in a Substring of Given Length
Hint
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""

class Solution(object):
    def max_vowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        start_index = 0
        end_index = 0
        maxvalue = 0
        counter = 0

        vowels = "aeiou"

        while end_index < len(s):
            current_char = s[end_index].lower()  # Convert the current character to lowercase

            # Check if the current character is a vowel
            if current_char in vowels:
                counter += 1

            end_index += 1

            if end_index - start_index > k:
                # If the window size exceeds k, update the start index and counter
                start_char = s[start_index].lower()  # Convert the start character to lowercase

                if start_char in vowels:
                    counter -= 1

                start_index += 1

            maxvalue = max(maxvalue, counter)

        return maxvalue


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
result = solution_instance.max_vowels("abciiidef", 3)
assert result == 3, "should be equal to 3"

result = solution_instance.max_vowels("aeiou", 2)
assert result == 2, "should be equal to 3"

result = solution_instance.max_vowels("leetcode", 3)
assert result == 2, "should be equal to 2"
