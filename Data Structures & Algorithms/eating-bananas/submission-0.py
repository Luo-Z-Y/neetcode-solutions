class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)     
            
            if hours <= h:
                right = mid              # mid works, the answer is mid or slower
            else:
                left = mid + 1           # too slow
        return left