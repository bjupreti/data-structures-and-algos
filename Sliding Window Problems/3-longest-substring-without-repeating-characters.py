import unittest

"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        # longest_substring = 0
        # for i in range(len(s)):
        #     substring = ""
        #     for j in s[i:]:
        #         current = j
        #         if current not in substring:
        #             substring += current
        #             longest_substring = max(longest_substring, len(substring))
        #         else:
        #             break

        # return longest_substring

        # Sliding Window approach
        left = 0
        longest_substring_len = 0
        for right in range(len(s)):
            temp_s = s[left:right]
            current_char = s[right]

            while current_char in temp_s:
                temp_s = s[left + 1 : right]
                left += 1
            longest_substring_len = max(longest_substring_len, right + 1 - left)

        return longest_substring_len


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_abcabcbb(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_bbbbb(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_pwwkew(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)


if __name__ == "__main__":
    unittest.main()
