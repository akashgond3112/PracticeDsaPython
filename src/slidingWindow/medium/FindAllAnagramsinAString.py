"""
 * @author agond
 * @package main.slidingWindow.medium
 * @Date 17/10/2023
 * @Project PracticeDSA
 *
 * 438. Find All Anagrams in a String
 * Medium
 * Topics
 * Companies
 * Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 *
 * Example 1:
 *
 * Input: s = "cbaebabacd", p = "abc"
 * Output: [0,6]
 * Explanation:
 * The substring with start index = 0 is "cba", which is an anagram of "abc".
 * The substring with start index = 6 is "bac", which is an anagram of "abc".
 * Example 2:
 *
 * Input: s = "abab", p = "ab"
 * Output: [0,1,2]
 * Explanation:
 * The substring with start index = 0 is "ab", which is an anagram of "ab".
 * The substring with start index = 1 is "ba", which is an anagram of "ab".
 * The substring with start index = 2 is "ab", which is an anagram of "ab".
 *
 * Constraints:
 *
 * 1 <= s.length, p.length <= 3 * 104
 * s and p consist of lowercase English letters.
"""
from collections import defaultdict


class Solution(object):
    def findAnagrams(self, txt, pat):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        start_index = 0
        end_index = 0
        ans = []

        if len(txt) <= 0 or len(pat) <= 0:
            return ans

        char_count = defaultdict(int)

        for char in pat:
            char_count[char] += 1
        cnt = len(char_count)

        while end_index < len(txt):
            current_char = txt[end_index]
            count = char_count.get(current_char, 0) - 1
            char_count[current_char] = count
            if count == 0:
                cnt -= 1

            if end_index - start_index + 1 < len(pat):
                end_index += 1
            elif end_index - start_index + 1 == len(pat):
                if cnt == 0:
                    ans.append(start_index)

                # Reverse the changes
                current_char = txt[start_index]
                count = char_count.get(current_char, 0) + 1
                char_count[current_char] = count
                if count == 1:
                    cnt += 1

                start_index += 1
                end_index += 1

        return ans
