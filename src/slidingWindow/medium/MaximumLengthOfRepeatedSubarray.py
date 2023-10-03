"""
* @author agond
* @package main.slidingWindow.medium
* @Date 02/10/2023
* @Project PracticeDSA
* <p>
* 718. Maximum Length of Repeated Subarray
* Medium
* Topics
* Companies
* Hint
* Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
* <p>
* Example 1:
* <p>
* Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
* Output: 3
* Explanation: The repeated subarray with maximum length is [3,2,1].
* Example 2:
* <p>
* Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
* Output: 5
* Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
* <p>
* Constraints:
* <p>
* 1 <= nums1.length, nums2.length <= 1000
* 0 <= nums1[i], nums2[i] <= 100
"""


class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)

        # Initialize a table to store common subarray lengths
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        max_len = 0

        # Fill the dp table based on dynamic programming
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])

        return max_len


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]
result = solution_instance.findLength(nums1, nums2)

assert result == 3, "Test 1, should be equal to 3."
