from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #step 1: find a window that contains the substring by expanding the right, record the length of the window
        # try to shrink the left until we could not do so anymore (but we shrink one more)
        # expand the right until the window is valid again, record the length and compare with previous length
        # repeat the process

        need = Counter(t)
        have = defaultdict(int)
        unsatisfied = len(need)
        best_len = float('inf')
        left = opt_left = opt_right = 0

        for right, c in enumerate(s):
            if c not in need:
                continue
            have[c] += 1
            if have[c] != need[c]:
                continue
            unsatisfied -= 1
            if unsatisfied:                      # one count hit its target; window still not valid
                continue
            while s[left] not in need or have[s[left]] > need[s[left]]:
                if have[s[left]] > need[s[left]]:
                    have[s[left]] -= 1
                left += 1 
            # after shrinking, get cur len, and compare
            if right - left + 1 < best_len:
                best_len = right - left + 1
                opt_left, opt_right = left, right
            # delete one more to make it invalid again
            have[s[left]] -= 1
            unsatisfied += 1
            left += 1
        
        return "" if best_len == float('inf') else s[opt_left:opt_right + 1]


