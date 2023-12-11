"""
 * @author agond
 * @package main.slidingWindow.medium
 * @Date 11/12/2023
 * @Project PracticeDSA
 * <p>
 * 978. Longest Turbulent Subarray
 * Medium
 * Topics
 * Companies
 * Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
 * <p>
 * A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
 * <p>
 * More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
 * <p>
 * For i <= k < j:
 * arr[k] > arr[k + 1] when k is odd, and
 * arr[k] < arr[k + 1] when k is even.
 * Or, for i <= k < j:
 * arr[k] > arr[k + 1] when k is even, and
 * arr[k] < arr[k + 1] when k is odd.
 * <p>
 * Example 1:
 * <p>
 * Input: arr = [9,4,2,10,7,8,8,1,9]
 * Output: 5
 * Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
 * Example 2:
 * <p>
 * Input: arr = [4,8,12,16]
 * Output: 2
 * Example 3:
 * <p>
 * Input: arr = [100]
 * Output: 1
 * <p>
 * Constraints:
 * <p>
 * 1 <= arr.length <= 4 * 104
 * 0 <= arr[i] <= 109
"""


class LongestTurbulentSubarray(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return 1

        start_index = 0
        end_index = 1
        max_length = 1
        prev_cmp = 1 if arr[1] > arr[0] else -1 if arr[1] < arr[0] else 0

        while end_index < len(arr):
            cmp_result = (arr[end_index] > arr[end_index - 1]) - (arr[end_index] < arr[end_index - 1])

            if cmp_result == 0:
                start_index = end_index
            elif cmp_result == prev_cmp:
                start_index = end_index-1
            max_length = max(max_length, end_index - start_index + 1)
            prev_cmp = cmp_result
            end_index += 1

        return max_length


# Create an instance of the Solution class
solution_instance = LongestTurbulentSubarray()

# Call the maxVowels method with the appropriate arguments
nums = [8, 2, 4, 7]
result = solution_instance.maxTurbulenceSize(nums)

assert result == 5, "Test 1, should be equal to 5."
