/**
 * LeetCode #1: Two Sum
 * Difficulty: Easy
 * Language: Python
 * Date: 2026-09-30T17:21:21.921Z
 */

class Solution:
    def twoSum(self, nums ,target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num 
            if complement in seen:
                return[seen[complement], i]
            seen[num] = i
        return []

