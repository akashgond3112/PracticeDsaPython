"""
* @author agond
 * @package main.slidingWindow.medium
 * @Date 24/10/2023
 * @Project PracticeDSA
 * <p>
 * 2401. Longest Nice Subarray
 * Medium
 * Topics
 * Companies
 * Hint
 * You are given an array nums consisting of positive integers.
 * <p>
 * We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.
 * <p>
 * Return the length of the longest nice subarray.
 * <p>
 * A subarray is a contiguous part of an array.
 * <p>
 * Note that subarrays of length 1 are always considered nice.
 * <p>
 * Example 1:
 * <p>
 * Input: nums = [1,3,8,48,10]
 * Output: 3
 * Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
 * - 3 AND 8 = 0.
 * - 3 AND 48 = 0.
 * - 8 AND 48 = 0.
 * It can be proven that no longer nice subarray can be obtained, so we return 3.
 * Example 2:
 * <p>
 * Input: nums = [3,1,5,11,13]
 * Output: 1
 * Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
 * <p>
 * Constraints:
 * 1 <= nums.length <= 105
 * 1 <= nums[i] <= 109
"""


class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_index = 0
        end_index = 0
        max_length = 0
        count = 0

        while end_index < len(nums):
            while count & nums[end_index] != 0:
                count ^= nums[start_index]
                start_index += 1

            count |= nums[end_index]

            max_length = max(max_length, end_index - start_index + 1)
            end_index += 1

        return max_length


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
arr = [1, 3, 8, 48, 10]
result = solution_instance.longestNiceSubarray(arr)

assert result == 3, "Test 1, should be equal to 3."

arr = [3, 1, 5, 11, 13]
result = solution_instance.longestNiceSubarray(arr)
assert result == 1, "Test 2, should be equal to 1."
