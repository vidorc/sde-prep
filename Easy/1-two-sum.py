/**
 * LeetCode #1: Two Sum
 * Difficulty: Easy
 * Language: Python
 * Date: 2026-09-30T17:52:09.824Z
 */

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True 
            seen.add(num)
        return False