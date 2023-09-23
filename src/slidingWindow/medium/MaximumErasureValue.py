"""
* @author agond
* @package main.slidingWindow.medium
* @Date 23/09/2023
* @Project PracticeDSA

1695. Maximum Erasure Value
Hint
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
"""


class Solution(object):
    def maximum_unique_subarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start_index = 0
        end_index = 0
        max_value = 0
        result = 0

        integer_dic = {}

        while end_index < len(nums):
            if nums[end_index] in integer_dic:
                integer_dic[nums[end_index]] += 1
            else:
                integer_dic[nums[end_index]] = 1

            result += nums[end_index]

            while integer_dic[nums[end_index]] > 1:
                result -= nums[start_index]
                if nums[start_index] in integer_dic:
                    integer_dic[nums[start_index]] -= 1
                else:
                    integer_dic[nums[start_index]] = 0
                if nums[start_index] == 0:
                    integer_dic.pop(nums[start_index])

                start_index += 1

            end_index += 1
            max_value = max(max_value, result)
        return max_value


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
arr = [4, 2, 4, 5, 6]
result = solution_instance.maximum_unique_subarray(arr)

assert result == 17, "Test 1, should be equal to 17."

arr = [5, 2, 1, 2, 5, 2, 1, 2, 5]
result = solution_instance.maximum_unique_subarray(arr)
assert result == 8, "Test 2, should be equal to 9."
