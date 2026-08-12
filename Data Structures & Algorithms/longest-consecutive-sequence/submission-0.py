class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        nums_set = set(nums)
        
        for num in nums:
            if num - 1 in nums_set:
                continue
            else:
                cur_len = 1
                cur_num = num
                while cur_num + 1 in nums_set:
                    cur_len += 1
                    cur_num += 1
                longest = max(longest, cur_len)
        return longest
