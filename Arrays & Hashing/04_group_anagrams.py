"""
Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
# Solution goes below
from typing import List
class Solution:
    # brute force solution
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sorted_anagrams:
                sorted_anagrams[sorted_s].append(s)
            else:
                sorted_anagrams[sorted_s] = [s]
        return list(sorted_anagrams.values())
    # optimized solution using defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        sorted_anagrams = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            sorted_anagrams[sorted_s].append(s)  # No need for if/else
        return list(sorted_anagrams.values())

# testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(sol.groupAnagrams([""]))
    # Output: [[""]]
    print(sol.groupAnagrams(["a"]))
    # Output: [["a"]]