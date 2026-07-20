class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        min_ending=nums[0]
        max_ending=nums[0]
        res=nums[0]
        for i in range(1,n):
            v1=min_ending * nums[i]
            v2=max_ending * nums[i]
            v3= nums[i]
            max_ending=max(v1,max(v2,v3))
            min_ending=min(v1,min(v2,v3))

            res = max(res,max(max_ending,min_ending))

        return res