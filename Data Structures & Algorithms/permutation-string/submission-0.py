class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        s1_len = len(s1)
        left = 0
        window_freq = defaultdict(int)

        for right, c in enumerate(s2):
            window_freq[c] += 1
            if right - left + 1 > s1_len:          # one too wide: drop the left char
                window_freq[s2[left]] -= 1
                if window_freq[s2[left]] == 0:
                    del window_freq[s2[left]]
                left += 1
            if window_freq == s1_freq:
                return True
        return False