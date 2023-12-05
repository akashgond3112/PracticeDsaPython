"""
* @author agond
* @package main.slidingWindow.medium
* @Date 05/12/2023
* @Project PracticeDSA
* <p>
* 187. Repeated DNA Sequences
* Medium
* Topics
* Companies
* The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
* <p>
* For example, "ACGAATTCCG" is a DNA sequence.
* When studying DNA, it is useful to identify repeated sequences within the DNA.
* <p>
* Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
* You may return the answer in any order.
* <p>
* Example 1:
* Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
* Output: ["AAAAACCCCC","CCCCCAAAAA"]
* <p>
* Example 2:
* Input: s = "AAAAAAAAAAAAA"
* Output: ["AAAAAAAAAA"]
* <p>
* Constraints:
* 1 <= s.length <= 105
* s[i] is either 'A', 'C', 'G', or 'T'.
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen_substrings = set()
        repeated_sequences = set()
        end_index = 0

        while end_index <= len(s) - 10:
            substring = s[end_index:end_index + 10]
            if substring in seen_substrings:
                repeated_sequences.add(substring)
            seen_substrings.add(substring)
            end_index += 1

        return list(repeated_sequences)


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result_substrings = set()
result_substrings.add("AAAAACCCCC")
result_substrings.add("CCCCCAAAAA")
result = solution_instance.findRepeatedDnaSequences(s)

assert result == result_substrings, "Test 1, should be equal to ['AAAAACCCCC','CCCCCAAAAA']."
