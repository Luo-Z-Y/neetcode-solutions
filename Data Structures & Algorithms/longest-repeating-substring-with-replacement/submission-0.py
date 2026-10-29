from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = longest = 0
        in_window = defaultdict(int)

        for i, c in enumerate(s):
            in_window[c] += 1
            if i - left + 1 - k <= max(in_window.values()):
                longest = max(longest, i - left + 1)
            else:
                in_window[s[left]] -= 1
                left += 1
        return longest