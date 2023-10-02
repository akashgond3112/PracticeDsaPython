"""
* @author agond
 * @package main.slidingWindow.medium
 * @Date 02/10/2023
 * @Project PracticeDSA
 * <p>
 * 2134. Minimum Swaps to Group All 1's Together II
 * Medium
 * Topics
 * Companies
 * Hint
 * A swap is defined as taking two distinct positions in an array and swapping the values in them.
 * <p>
 * A circular array is defined as an array where we consider the first element and the last element to be adjacent.
 * <p>
 * Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.
 * <p>
 * Example 1:
 * <p>
 * Input: nums = [0,1,0,1,1,0,0]
 * Output: 1
 * Explanation: Here are a few of the ways to group all the 1's together:
 * [0,0,1,1,1,0,0] using 1 swap.
 * [0,1,1,1,0,0,0] using 1 swap.
 * [1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
 * There is no way to group all 1's together with 0 swaps.
 * Thus, the minimum number of swaps required is 1.
 * Example 2:
 * <p>
 * Input: nums = [0,1,1,1,0,0,1,1,0]
 * Output: 2
 * Explanation: Here are a few of the ways to group all the 1's together:
 * [1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
 * [1,1,1,1,1,0,0,0,0] using 2 swaps.
 * There is no way to group all 1's together with 0 or 1 swaps.
 * Thus, the minimum number of swaps required is 2.
 * Example 3:
 * <p>
 * Input: nums = [1,1,0,0,1]
 * Output: 0
 * Explanation: All the 1's are already grouped together due to the circular property of the array.
 * Thus, the minimum number of swaps required is 0.
 * <p>
 * Constraints:
 * <p>
 * 1 <= nums.length <= 105
 * nums[i] is either 0 or 1.
"""


class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_ones = 0
        for one in nums:
            if one == 1:
                total_ones += 1

        n = len(nums)
        start_index = 0
        end_index = 0
        current_window_ones = 0
        swaps = n

        while end_index < 2 * n:

            if end_index < total_ones:
                if nums[end_index] == 1:
                    current_window_ones += 1

                end_index += 1
                swaps = total_ones - current_window_ones
            else:
                if nums[start_index % n] == 1:
                    current_window_ones -= 1

                if nums[end_index % n] == 1:
                    current_window_ones += 1

                start_index += 1
                end_index += 1

                swaps = min(swaps, total_ones - current_window_ones)

        return swaps


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
arr = [0, 1, 0, 1, 1, 0, 0]
result = solution_instance.minSwaps(arr)

assert result == 1, "Test 1, should be equal to 1."
