"""
 * @author agond
 * @package main.slidingWindow.medium
 * @Date 04/12/2023
 * @Project PracticeDSA
 * 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
 * Medium
 * Topics
 * Companies
 * Hint
 * Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
 * <p>
 * Example 1:
 * <p>
 * Input: nums = [8,2,4,7], limit = 4
 * Output: 2
 * Explanation: All subarrays are:
 * [8] with maximum absolute diff |8-8| = 0 <= 4.
 * [8,2] with maximum absolute diff |8-2| = 6 > 4.
 * [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
 * [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
 * [2] with maximum absolute diff |2-2| = 0 <= 4.
 * [2,4] with maximum absolute diff |2-4| = 2 <= 4.
 * [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
 * [4] with maximum absolute diff |4-4| = 0 <= 4.
 * [4,7] with maximum absolute diff |4-7| = 3 <= 4.
 * [7] with maximum absolute diff |7-7| = 0 <= 4.
 * Therefore, the size of the longest subarray is 2.
 * Example 2:
 * <p>
 * Input: nums = [10,1,2,4,7,2], limit = 5
 * Output: 4
 * Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
 * Example 3:
 * <p>
 * Input: nums = [4,2,2,2,4,4,2,2], limit = 0
 * Output: 3
 * <p>
 * Constraints:
 * 1 <= nums.length <= 105
 * 1 <= nums[i] <= 109
 * 0 <= limit <= 109
"""

from collections import deque


class Solution(object):

    def longest_subarray(self, nums, limit):
        maxDeque = deque()  # to store the maximum values in the current window
        minDeque = deque()  # to store the minimum values in the current window
        l = 0
        mlen = 0

        for r in range(len(nums)):
            # Update maxDeque with the current maximum value
            while maxDeque and nums[r] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[r])

            # Update minDeque with the current minimum value
            while minDeque and nums[r] < minDeque[-1]:
                minDeque.pop()
            minDeque.append(nums[r])

            # Check if the absolute difference exceeds the limit
            while maxDeque[0] - minDeque[0] > limit:
                # Move the left pointer to the right
                if maxDeque[0] == nums[l]:
                    maxDeque.popleft()
                if minDeque[0] == nums[l]:
                    minDeque.popleft()
                l += 1

            # Update the maximum length of subarray
            mlen = max(mlen, r - l + 1)

        return mlen


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
nums = [8, 2, 4, 7]
limit = 4
result = solution_instance.longest_subarray(nums, limit)

assert result == 2, "Test 1, should be equal to 3."
