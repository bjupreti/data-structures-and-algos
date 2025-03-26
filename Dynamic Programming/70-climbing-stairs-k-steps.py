"""
70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.

Each time you can climb upto k steps. In how many distinct ways can you climb to the top?



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
    def climb_stairs_k_steps(self, n: int, k: int) -> int:
        if n <= 0 or k <= 0:
            raise ValueError("n and k must be positive integers.")

        dp = [1] + [0] * k  # only store the last k values
        # window_sum = 1  # sum of last 'k' elments

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                if i >= j:
                    dp[i % k] += dp[i - j]
        return dp[k]


"""
Time Complexity: 
O(n*k) Because we iterate through n times and for each iteration we run another loop for k times.

Space Complexity: 
O(n) Because we store n number in dp array
"""


class TestClimbStairsSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.correct_input_and_output = [(1, 4, 1), (2, 4, 2), (5, 4, 15)]

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            self.solution.climb_stairs_k_steps(-1, 4)

    def test_input_is_0(self):
        with self.assertRaises(ValueError):
            self.solution.climb_stairs_k_steps(0, 4)

    def test_correct_input_and_output(self):
        for n, k, test_output in self.correct_input_and_output:
            self.assertEqual(self.solution.climb_stairs_k_steps(n, k), test_output)
            print(n, k, test_output)
            print("pass")


if __name__ == "__main__":
    unittest.main()
