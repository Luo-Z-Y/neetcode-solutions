class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [] 
       
        prefix = [1] * length
        suffix = [1] * length
        p = 1
        s = 1

        for i in range(1, length):
            p *= nums[i-1]
            prefix[i] = p
            s *= nums[length-i]
            suffix[length-1-i] = s

        for i in range(length):
            res.append(prefix[i] * suffix[i])
        return res