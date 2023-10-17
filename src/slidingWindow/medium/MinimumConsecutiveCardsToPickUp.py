"""

"""


class Solution:
    def minimumCardPickup(self, cards):
        result = float('inf')
        end_index = 0
        start_index = 0
        integer_map = {}

        while end_index < len(cards):
            if cards[end_index] in integer_map:
                integer_map[cards[end_index]] += 1
            else:
                integer_map[cards[end_index]] = 1

            while integer_map[cards[end_index]] > 1:
                result = min(result, end_index - start_index + 1)
                integer_map[cards[start_index]] -= 1

                if integer_map[cards[start_index]] == 0:
                    del integer_map[cards[start_index]]

                start_index += 1
            end_index += 1

        if result == float('inf'):
            return -1
        return result


# Create an instance of the Solution class
solution_instance = Solution()

# Call the maxVowels method with the appropriate arguments
nums1 = [1, 2, 3, 2, 1]
ans = solution_instance.minimumCardPickup(nums1)
assert ans == 4, "Test 1, should be equal to 4."

nums1 = [1, 0, 5, 3]
ans = solution_instance.minimumCardPickup(nums1)
assert ans == -1, "Test 2, should be equal to -1."

nums1 = [95, 11, 8, 65, 5, 86, 30, 27, 30, 73, 15, 91, 30, 7, 37, 26, 55, 76, 60, 43, 36, 85, 47, 96, 6]
ans = solution_instance.minimumCardPickup(nums1)
assert ans == 3, "Test 3, should be equal to 3."
