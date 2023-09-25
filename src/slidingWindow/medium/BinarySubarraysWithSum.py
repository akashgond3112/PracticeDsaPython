
"""
* @author agond
* @package main.slidingWindow.medium
* @Date 25/09/2023
* @Project PracticeDSA
* <p>
* 930. Binary Subarrays With Sum
* Medium
* Topics
* Companies
* Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
* <p>
* A subarray is a contiguous part of the array.
* <p>
* Example 1:
* <p>
* Input: nums = [1,0,1,0,1], goal = 2
* Output: 4
* Explanation: The 4 subarrays are bolded and underlined below:
* [1,0,1,0,1]
* [1,0,1,0,1]
* [1,0,1,0,1]
* [1,0,1,0,1]
* Example 2:
* <p>
* Input: nums = [0,0,0,0,0], goal = 0
* Output: 15
* <p>
* Constraints:
* <p>
* 1 <= nums.length <= 3 * 104
* nums[i] is either 0 or 1.
* 0 <= goal <= nums.length
"""
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = 0
        total_sum = 0
        sum_counts = {0: 1}

        for num in nums:
            total_sum += num
            count += sum_counts.get(total_sum - goal, 0)
            sum_counts[total_sum] = sum_counts.get(total_sum, 0) + 1

        return count


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
arr = [1, 0, 1, 0, 1]
goal = 2
result = solution_instance.numSubarraysWithSum(arr, goal)

assert result == 4, "Test 1, should be equal to 4."

arr = [0, 0, 0, 0, 0]
goal = 0
result = solution_instance.numSubarraysWithSum(arr, goal)
assert result == 15, "Test 2, should be equal to 15."
