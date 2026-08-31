class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLength = 0
        l = 0
        longest = set()

        for r in range(len(s)):
            while s[r] in longest:
                longest.remove(s[l])
                l += 1
            longest.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength




