class Solution:
    def maxsumarr(self,nums):
        n=len(nums)
        bestending=nums[0]
        res=nums[0]
        for i in range(1,n):
            v1=bestending+nums[i]
            v2=nums[i]
            bestending=max(v1,v2)
            res=max(res,bestending)
        return res
    def minsumarr(self,nums):
        n=len(nums)
        bestending=nums[0]
        res=nums[0]
        for i in range(1,n):
            v1=bestending+nums[i]
            v2=nums[i]
            bestending=min(v1,v2)
            res=min(res,bestending)
        return res
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        sum_array = 0
        for i in range(0,n):
            sum_array+=nums[i]
        A1=self.maxsumarr(nums)
        if A1 < 0:
            return A1

        A2=sum_array - (self.minsumarr(nums))

        return max(A1,A2)
        