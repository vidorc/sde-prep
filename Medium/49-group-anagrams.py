/**
 * LeetCode #49: Group Anagrams
 * Difficulty: Medium
 * Language: Python
 * Date: 2026-09-30T19:16:50.429Z
 */

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())