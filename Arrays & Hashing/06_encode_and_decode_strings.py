"""
Encode and Decode Strings

Design an algorithm to encode a list of strings to a string and decode it back to the list of strings.

Example 1:
Input: strs = ["lint","code","love","you"]
Output: ["lint","code","love","you"]

Example 2:
Input: strs = ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any possible characters out of 256 valid ascii characters.
"""
# Solution goes below
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            break
        return res

# testing
if __name__ == "__main__":
    sol = Solution()
    encoded = sol.encode(["lint","code","love","you"])
    print(encoded)  # Output: "4#lint4#code4#love3#you"
    decoded = sol.decode(encoded)
    # print(decoded)  # Output: ["lint","code","love","you"]

    # encoded2 = sol.encode(["we","say",":","yes"])
    # print(encoded2)  # Output: "2#we3#say1#:3#yes"
    # decoded2 = sol.decode(encoded2)
    # print(decoded2)  # Output: ["we","say",":","yes"]