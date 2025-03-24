"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
"""

import unittest


class Solution:
    def climb_stairs(self, n: int) -> int:
        if n <= 0:
            raise ValueError(f"Input must be greater than 0. Passed {n}")

        if n < 2:
            return n

        prev_two = 1
        prev_one = 2
        result = 0

        for i in range(3, n + 1):
            result = prev_two + prev_one
            prev_one, prev_two = result, prev_one

        return result


"""
Time Complexity: O(n) -> Iterates through n
Space Complexity: O(1) -> Uses only two variables

"""


class TestClimbStairsSolution(unittest.TestCase):
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            solution = Solution()
            solution.climb_stairs(-1)

    def test_input_is_0(self):
        with self.assertRaises(ValueError):
            solution = Solution()
            solution.climb_stairs(-1)

    def test_input_is_1(self):
        solution = Solution()
        self.assertEqual(solution.climb_stairs(1), 1)

    def test_input_is_5(self):
        solution = Solution()
        self.assertEqual(solution.climb_stairs(5), 8)


if __name__ == "__main__":
    unittest.main()
