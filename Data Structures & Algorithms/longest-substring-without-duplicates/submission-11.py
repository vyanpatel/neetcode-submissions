class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 1
        l, r = 0, 1
        if len(s) == 0:
            return 0

        longest = set(s[l])

        while r < len(s) and l < len(s):
            if s[r] not in longest:
                longest.add(s[r])
                maxLength = max(len(longest), maxLength)
                r += 1
            else:
                longest.discard(s[l])
                l += 1

        return maxLength




