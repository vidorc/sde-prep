/**
 * LeetCode #217: Contains Duplicate
 * Difficulty: Easy
 * Language: Python
 * Date: 2026-09-30T18:11:12.807Z
 */

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True 
            seen.add(num)
        return False