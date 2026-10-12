/**
 * LeetCode #121: Best Time to Buy and Sell Stock
 * Difficulty: Easy
 * Language: Python
 * Date: 2026-10-12T23:39:29.878Z
 */

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_len = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len