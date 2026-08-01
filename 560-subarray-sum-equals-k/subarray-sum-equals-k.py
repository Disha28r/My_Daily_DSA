class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_tillnow = 0
        res = 0
        f = {0: 1} 
        for i in range(len(nums)):
            sum_tillnow += nums[i]
            sum_previousprefix = sum_tillnow - k
            freq = f.get(sum_previousprefix,0)
            res += freq
            
            f[sum_tillnow] = f.get(sum_tillnow, 0) + 1
            
        return res