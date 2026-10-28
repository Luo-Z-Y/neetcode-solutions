class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_appeared_at = {}
        left = 0
        longest = 0
        for i, c in enumerate(s):
            if c not in last_appeared_at or left > last_appeared_at[c]:
                longest= max(longest, i - left + 1)
            else:
                left = last_appeared_at[c] + 1
            last_appeared_at[c] = i
        return longest