/**
 * LeetCode #121: Best Time to Buy and Sell Stock
 * Difficulty: Easy
 * Language: Python
 * Date: 2026-10-13T00:24:29.867Z
 */

class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""
        
        start = 0
        max_len = 1
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        for i in range(len(s)):
            len1 = expand(i, i)        # odd length
            len2 = expand(i, i + 1)    # even length
            length = max(len1, len2)
            
            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2
        
        return s[start:start + max_len]