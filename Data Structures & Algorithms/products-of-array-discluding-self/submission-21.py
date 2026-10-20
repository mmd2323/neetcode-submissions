class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 1,1
        res = [1]* n
        for i, num in enumerate(nums):
            res [i] = left
            left = num * res[i]
        for i in range (1,n+1): 
            res[-i] *= right 
            right *= nums[-i]
        return res
            

        