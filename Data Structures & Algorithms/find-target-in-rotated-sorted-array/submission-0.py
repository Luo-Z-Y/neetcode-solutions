class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            mid_low = nums[mid] <= nums[r]        # is mid in the low run?
            tgt_low = target <= nums[r]           # is the target in the low run?
            if mid_low == tgt_low:                # same run: ordinary comparison is valid
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif mid_low:                         # mid in low run, target in high run
                r = mid - 1
            else:                                 # mid in high run, target in low run
                l = mid + 1
        return -1