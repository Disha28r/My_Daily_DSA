class Solution:
    def maxsum(self,nums):
        i=0
        bestending=nums[0]
        ans= nums[0]
        for i in range(1,len(nums)):
            v1=bestending+nums[i]
            v2=nums[i]
            bestending=max(v1,v2)
            ans=max(ans,bestending)
        return ans
    def minsum(self,nums):
        i=0
        bestending=nums[0]
        ans= nums[0]
        for i in range(1,len(nums)):
            v1=bestending+nums[i]
            v2=nums[i]
            bestending=min(v1,v2)
            ans=min(ans,bestending)
        return ans
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = self.maxsum(nums)
        min_sum = self.minsum(nums)

        return max(abs(max_sum), abs(min_sum))
        