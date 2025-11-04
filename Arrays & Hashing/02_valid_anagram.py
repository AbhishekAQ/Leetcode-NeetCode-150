"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""
# Solution goes below

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    # optimized solution
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    # optiomized solution using set
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True
# testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # Output: True
    print(sol.isAnagram("rat", "car"))          # Output: False