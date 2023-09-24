"""
/**
 * @author agond
 * @package main.slidingWindow.medium
 * @Date 24/09/2023
 * @Project PracticeDSA
 * <p>
 * 1052. Grumpy Bookstore Owner
 * Hint
 * There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store.
 * You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
 * <p>
 * On some minutes, the bookstore owner is grumpy.
 * You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
 * <p>
 * When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
 * <p>
 * The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
 * <p>
 * Return the maximum number of customers that can be satisfied throughout the day.
 * <p>
 * Example 1:
 * <p>
 * Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
 * Output: 16
 * Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
 * The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
 * Example 2:
 * <p>
 * Input: customers = [1], grumpy = [0], minutes = 1
 * Output: 1
 */
"""


class Solution(object):
    def max_satisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        satisfied = 0  # Total satisfied customers when the owner is not grumpy
        max_satisfied = 0  # Maximum satisfied customers during grumpy minutes
        window_sum = 0  # Current sum of customers during grumpy minutes
        right = 0  # Right pointer of the sliding window
        left = 0  # Left pointer of the sliding window

        while right < len(customers):

            if grumpy[right] == 0:
                satisfied += customers[right]
            else:
                window_sum += customers[right]

            while right - left + 1 > minutes:
                if grumpy[left] == 1:
                    window_sum -= customers[left]

                left += 1

            right += 1
            max_satisfied = max(max_satisfied, window_sum)

        return satisfied + max_satisfied


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
minutes = 3
result = solution_instance.max_satisfied(customers, grumpy, minutes)

assert result == 16, "Test 1, should be equal to 16."

customers = [1]
grumpy = [0]
minutes = 1
result = solution_instance.max_satisfied(customers, grumpy, minutes)
assert result == 1, "Test 2, should be equal to 1."
