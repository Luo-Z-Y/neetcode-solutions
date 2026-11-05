class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:            # this range is sorted: minimum is at l
                return nums[l]
            mid = (l + r) // 2
            if nums[mid] >= nums[l]:         # rotated and left half sorted: minimum is right of mid
                l = mid + 1
            else:                            # drop is in (l, mid]
                r = mid
        return nums[l]