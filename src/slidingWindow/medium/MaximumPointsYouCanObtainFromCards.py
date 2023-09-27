"""
* @author agond
* @package main.slidingWindow.medium
* @Date 26/09/2023
* @Project PracticeDSA
* <p>
* 1423. Maximum Points You Can Obtain from Cards
* Medium
* Topics
* Companies
* Hint
* There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
* <p>
* In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
* <p>
* Your score is the sum of the points of the cards you have taken.
* <p>
* Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
* <p>
* Example 1:
* <p>
* Input: cardPoints = [1,2,3,4,5,6,1], k = 3
* Output: 12
* Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
* Example 2:
* <p>
* Input: cardPoints = [2,2,2], k = 2
* Output: 4
* Explanation: Regardless of which two cards you take, your score will always be 4.
* Example 3:
* <p>
* Input: cardPoints = [9,7,7,9,7,7,9], k = 7
* Output: 55
* Explanation: You have to take all the cards. Your score is the sum of points of all cards.
* <p>
* <p>
* Constraints:
* <p>
* 1 <= cardPoints.length <= 10^5
* 1 <= cardPoints[i] <= 10^4
* 1 <= k <= cardPoints.length
"""


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """

        total_sum = 0
        x = len(cardPoints) - k
        for a in cardPoints:
            total_sum += a

        if x == 0:
            return total_sum

        start_index = 0
        end_index = 0
        temp = 0
        max_value = float('inf')

        while end_index < len(cardPoints):
            temp += cardPoints[end_index]

            if end_index - start_index + 1 == x:
                max_value = min(max_value, temp)
                temp -= cardPoints[start_index]
                start_index += 1

            end_index += 1

        return total_sum - max_value


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
cardPoints = [1, 2, 3, 4, 5, 6, 1]
goal = 3
result = solution_instance.maxScore(cardPoints, goal)

assert result == 12, "Test 1, should be equal to 12."

cardPoints = [2, 2, 2]
goal = 2
result = solution_instance.maxScore(cardPoints, goal)
assert result == 4, "Test 2, should be equal to 4."

cardPoints = [9, 7, 7, 9, 7, 7, 9]
goal = 7
result = solution_instance.maxScore(cardPoints, goal)
assert result == 55, "Test 2, should be equal to 55."
